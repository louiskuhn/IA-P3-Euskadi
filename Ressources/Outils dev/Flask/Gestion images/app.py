import os
from flask import Flask, url_for, render_template, request, flash, redirect
from werkzeug.utils import secure_filename
import base64

UPLOAD_FOLDER = os.path.join('static', 'image')

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/")
def image():
    return render_template("image.html")

@app.route("/", methods=["POST"])
def upload():
    img = request.files["image"]

    #sans sauvegarde de l'image
    base64img = "data:image/png;base64,"+base64.b64encode(img.getvalue()).decode('ascii')

    #avec sauvegarde de l'image
    filename = secure_filename(img.filename)
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    img.save(full_filename)

    return render_template("image.html", full_filename=full_filename, base64img=base64img)

if __name__ == "__main__":
    app.run(debug=True)
    
