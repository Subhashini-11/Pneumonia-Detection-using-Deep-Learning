import os
import numpy as np
from flask import Flask, request, render_template, redirect, url_for, flash
from werkzeug.utils import secure_filename
from predict import process_image, make_prediction

# Create Flask app
app = Flask(__name__)
app.secret_key = "hellohahd54186behbhjbaebcu"

# Configure upload folder
UPLOAD_FOLDER = "static/uploads"
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg"}

# Create upload directory if it doesn't exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


# Function to check if file has allowed extension
def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


# Routes
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload_file():
    # Check if a file was submitted
    if "file" not in request.files:
        flash("No file part")
        return redirect(request.url)

    file = request.files["file"]

    # If user doesn't select file, browser also submits an empty part
    if file.filename == "":
        flash("No selected file")
        return redirect(request.url)

    # If file is valid and allowed
    if file and allowed_file(file.filename):
        # Save file
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
        file.save(file_path)

        # Process the image and make prediction
        processed_image = process_image(file_path)
        prediction, confidence = make_prediction(processed_image)

        # Render result page with prediction
        return render_template(
            "result.html",
            filename=filename,
            prediction=prediction,
            confidence=confidence,
            file_path=os.path.join(app.config["UPLOAD_FOLDER"], filename),
        )

    flash("Invalid file type. Please upload a PNG, JPG, or JPEG image.")
    return redirect(url_for("home"))


@app.route("/prevention")
def prevention():
    return render_template("prevention.html")


@app.route("/measures")
def measures():
    return render_template("measures.html")


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)
