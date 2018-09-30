from flask import Flask, render_template, request
from flask_dropzone import Dropzone
from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class
import os

app = Flask(__name__)

# dropzone for images
dropzone = Dropzone(app)
app.config["DROPZONE_UPLOAD_MULTIPLE"]     = False
app.config["DROPZONE_ALLOWED_FILE_CUSTOM"] = True
app.config["DROPZONE_ALLOWED_FILE_TYPE"]   = "image/*"
app.config["DROPZONE_REDIRECT_VIEW"]       = "results"

# upload
app.config["UPLOAD_PHOTOS_DEST"] = os.path.join(os.getcwd(), "uploads")
photo = UploadSet("photo", IMAGES)
configure_uploads(app, photo)
patch_request_class(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/results")
def results():
    return render_template("results.html")
