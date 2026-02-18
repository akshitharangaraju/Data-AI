from flask import Flask, request, jsonify, render_template
import os
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import (
    JWTManager, create_access_token,
    jwt_required, get_jwt_identity
)
from werkzeug.security import generate_password_hash, check_password_hash
from pydantic import BaseModel, ValidationError, Field

app = Flask(__name__)

# -----------------------------
# CONFIG
# -----------------------------
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'instance', 'products.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'supersecretkey'

db = SQLAlchemy(app)
jwt = JWTManager(app)

# -----------------------------
# PYDANTIC SCHEMAS
# -----------------------------
class RegisterSchema(BaseModel):
    username: str = Field(min_length=3)
    password: str = Field(min_length=4)

class LoginSchema(BaseModel):
    username: str
    password: str

# -----------------------------
# DATABASE MODELS
# -----------------------------
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    price = db.Column(db.Float)
    quantity = db.Column(db.Integer)

class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    product_id = db.Column(db.Integer)
    quantity = db.Column(db.Integer)

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    total_amount = db.Column(db.Float)

with app.app_context():
    db.create_all()

# =============================
# UI ROUTES (HTML)
# =============================
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/login")
def login_page():
    return render_template("login.html")

@app.route("/register")
def register_page():
    return render_template("register.html")

@app.route("/products")
def products_page():
    return render_template("products.html")

@app.route("/cart")
def cart_page():
    return render_template("cart.html")

@app.route("/checkout")
def checkout_page():
    return render_template("checkout.html")

# =============================
# AUTH APIs
# =============================
@app.route("/api/register", methods=["POST"])
def register_api():
    try:
        data = RegisterSchema(**request.json)
    except ValidationError as e:
        return jsonify(e.errors()), 400

    if User.query.filter_by(username=data.username).first():
        return jsonify({"msg": "User exists"}), 400

    hashed = generate_password_hash(data.password)
    db.session.add(User(username=data.username, password=hashed))
    db.session.commit()
    return jsonify({"msg": "Registered successfully"})

@app.route("/api/login", methods=["POST"])
def login_api():
    try:
        data = LoginSchema(**request.json)
    except ValidationError:
        return jsonify({"msg": "Invalid input"}), 400

    user = User.query.filter_by(username=data.username).first()
    if not user or not check_password_hash(user.password, data.password):
        return jsonify({"msg": "Invalid credentials"}), 401

    token = create_access_token(identity=data.username)
    return jsonify({"access_token": token})

# =============================
# PRODUCT APIs
# =============================
@app.route("/api/products", methods=["GET"])
@jwt_required()
def products_api():
    return jsonify([{
        "id": p.id,
        "name": p.name,
        "price": p.price,
        "quantity": p.quantity
    } for p in Product.query.all()])

# =============================
# CART APIs
# =============================
@app.route("/api/add_to_cart/<int:product_id>", methods=["POST"])
@jwt_required()
def add_to_cart_api(product_id):
    username = get_jwt_identity()
    qty = request.json.get("quantity", 1)

    db.session.add(Cart(username=username, product_id=product_id, quantity=qty))
    db.session.commit()
    return jsonify({"msg": "Added to cart"})

@app.route("/api/cart", methods=["GET"])
@jwt_required()
def cart_api():
    username = get_jwt_identity()
    items = Cart.query.filter_by(username=username).all()

    output = []
    total = 0
    for i in items:
        product = Product.query.get(i.product_id)
        item_total = product.price * i.quantity
        total += item_total
        output.append({
            "product": product.name,
            "qty": i.quantity,
            "total": item_total
        })

    return jsonify({"cart": output, "cart_total": total})

# =============================
# CHECKOUT API
# =============================
@app.route("/api/checkout", methods=["POST"])
@jwt_required()
def checkout_api():
    username = get_jwt_identity()
    items = Cart.query.filter_by(username=username).all()

    if not items:
        return jsonify({"msg": "Cart empty"}), 400

    total = sum(Product.query.get(i.product_id).price * i.quantity for i in items)

    db.session.add(Order(username=username, total_amount=total))
    Cart.query.filter_by(username=username).delete()
    db.session.commit()

    return jsonify({"msg": "Order placed", "total_paid": total})

# -----------------------------
# RUN
# -----------------------------
if __name__ == "__main__":
    app.run(debug=True)
