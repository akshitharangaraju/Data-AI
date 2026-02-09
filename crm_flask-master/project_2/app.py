import os
from flask import Flask, render_template, request, redirect, url_for, abort
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.utils import secure_filename
from extensions import db, login_manager
from models import User, Product, Cart, Order, OrderItem

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret123"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["UPLOAD_FOLDER"] = os.path.join(BASE_DIR, "static", "uploads")

db.init_app(app)
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# ---------------- PRODUCTS ----------------
@app.route("/")
@login_required
def products():
    search = request.args.get("search")
    max_price = request.args.get("price")

    query = Product.query
    if search:
        query = query.filter(Product.name.contains(search))
    if max_price:
        query = query.filter(Product.price <= max_price)

    return render_template("products.html", products=query.all())


# ---------------- AUTH ----------------
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        user = User(username=request.form["username"],
                    password=request.form["password"])
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("login"))
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = User.query.filter_by(
            username=request.form["username"],
            password=request.form["password"]
        ).first()

        if user:
            login_user(user)
            return redirect(url_for("products"))

    return render_template("login.html")


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("login"))


# ---------------- PRODUCT DETAIL ----------------
@app.route("/product/<int:product_id>")
@login_required
def product_detail(product_id):
    product = Product.query.get_or_404(product_id)
    return render_template("product_detail.html", product=product)


# ---------------- ADD TO CART ----------------
@app.route("/add-to-cart/<int:product_id>")
@login_required
def add_to_cart(product_id):
    item = Cart.query.filter_by(
        user_id=current_user.id,
        product_id=product_id
    ).first()

    if item:
        item.quantity += 1
    else:
        db.session.add(Cart(
            user_id=current_user.id,
            product_id=product_id,
            quantity=1
        ))

    db.session.commit()
    return redirect(url_for("view_cart"))


# ---------------- DELETE PRODUCT ----------------
@app.route("/delete-product/<int:product_id>")
@login_required
def delete_product(product_id):
    if not current_user.is_admin:
        return "Unauthorized", 403

    product = Product.query.get_or_404(product_id)

    Cart.query.filter_by(product_id=product_id).delete()
    OrderItem.query.filter_by(product_id=product_id).delete()

    db.session.delete(product)
    db.session.commit()

    return redirect(url_for("products"))


# ---------------- VIEW CART ----------------
@app.route("/cart")
@login_required
def view_cart():
    items = Cart.query.filter_by(user_id=current_user.id).all()
    total = sum(i.product.price * i.quantity for i in items)

    # NEW: get all products for related products section
    all_products = Product.query.all()

    return render_template(
        "cart.html",
        items=items,
        total=total,
        all_products=all_products
    )


# ---------------- CHECKOUT ----------------
@app.route("/checkout")
@login_required
def checkout():
    items = Cart.query.filter_by(user_id=current_user.id).all()
    if not items:
        return "Cart is empty"

    total = sum(i.product.price * i.quantity for i in items)

    order = Order(user_id=current_user.id, total_amount=total)
    db.session.add(order)
    db.session.flush()

    for i in items:
        db.session.add(OrderItem(
            order_id=order.id,
            product_id=i.product_id,
            quantity=i.quantity,
            price=i.product.price
        ))

    Cart.query.filter_by(user_id=current_user.id).delete()
    db.session.commit()

    return render_template("checkout_success.html", total=total)


# ---------------- ADD PRODUCT (ADMIN) ----------------
@app.route("/add-product", methods=["GET", "POST"])
@login_required
def add_product():
    if not current_user.is_admin:
        return "Unauthorized", 403

    if request.method == "POST":
        image = request.files["image"]
        filename = secure_filename(image.filename)
        image.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))

        product = Product(
            name=request.form["name"],
            price=request.form["price"],
            description=request.form["description"],
            image=filename
        )
        db.session.add(product)
        db.session.commit()
        return redirect(url_for("products"))

    return render_template("add_products.html")


# ---------------- MAIN ----------------
if __name__ == "__main__":
    os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)

    with app.app_context():
        db.create_all()

    app.run(debug=True)
