import os
from flask import Flask, request, render_template, send_from_directory
from werkzeug.utils import secure_filename

app = Flask(__name__)

# ---------- CONFIG ----------
UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif"}


# ---------- CHECK FILE TYPE ----------
def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


# ---------- BASIC ROUTES ----------
@app.route("/")
def home():
    return "Hello, Flask!"


@app.route("/about")
def about():
    return "About page"


@app.route("/user/<name>")
def user(name):
    return f"Hello {name}"


# ---------- TEMPLATE RENDER (/namm) ----------
@app.route("/namm")
def homes():
    return render_template("index.html", name="Akki")


# ---------- LOGIN (Simple placeholder) ----------
@app.route("/login", methods=["GET", "POST"])
def login():
    return "Login Page"


# ---------- FORM ----------
@app.route("/form")
def fo():
    return render_template("form.html")


@app.route("/submit", methods=["POST"])
def submit():
    username = request.form["username"]
    return f"Welcome {username}"


# ---------- IMAGE UPLOAD PAGE ----------
@app.route("/upload")
def upload_page():
    return render_template("upload.html")


# ---------- SAVE IMAGE ----------
@app.route("/upload_image", methods=["POST"])
def upload_image():
    if "image" not in request.files:
        return "No file selected"

    file = request.files["image"]

    if file.filename == "":
        return "No file selected"

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
        file.save(filepath)

        return render_template("upload.html", filename=filename)

    return "Invalid file type"


# ---------- DISPLAY IMAGE ----------
@app.route("/uploads/<filename>")
def uploaded_file(filename):
    return send_from_directory(app.config["UPLOAD_FOLDER"], filename)


# ---------- RUN ----------
if __name__ == "__main__":
    app.run(debug=True)
