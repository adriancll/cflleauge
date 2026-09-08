import os
import secrets
from functools import wraps
from pathlib import Path
from flask import Flask, abort, redirect, render_template, request, url_for
from PIL import Image, UnidentifiedImageError
from werkzeug.utils import secure_filename

app = Flask(__name__, static_url_path="")
app.config["MAX_CONTENT_LENGTH"] = 8 * 1024 * 1024
UPLOAD_FOLDER = Path(app.static_folder) / "uploads"
ALLOWED_EXTENSIONS = {".jpg", ".jpeg", ".png", ".gif", ".webp"}


def gallery_images():
    UPLOAD_FOLDER.mkdir(parents=True, exist_ok=True)
    return sorted(
        (image for image in UPLOAD_FOLDER.iterdir() if image.suffix.lower() in ALLOWED_EXTENSIONS),
        key=lambda image: image.stat().st_mtime,
        reverse=True,
    )


def require_admin(view):
    @wraps(view)
    def wrapped_view(*args, **kwargs):
        username = "fish"
        password = "hkfishingleauge2026"
        credentials = request.authorization

        if not username or not password:
            abort(503, "Set ADMIN_USERNAME and ADMIN_PASSWORD before using /admin.")

        authorized = credentials and secrets.compare_digest(credentials.username or "", username) and secrets.compare_digest(credentials.password or "", password)
        if not authorized:
            return ("Admin credentials required.", 401, {"WWW-Authenticate": 'Basic realm="HKCFL Admin"'})
        return view(*args, **kwargs)

    return wrapped_view


@app.get("/")
def home():
    return render_template("index.html", gallery_images=gallery_images())


@app.route("/admin", methods=["GET", "POST"])
@require_admin
def admin():
    error = None
    if request.method == "POST":
        upload = request.files.get("image")
        if not upload or not upload.filename:
            error = "Choose an image to upload."
        else:
            filename = secure_filename(upload.filename)
            extension = Path(filename).suffix.lower()
            if extension not in ALLOWED_EXTENSIONS:
                error = "Use a JPG, PNG, GIF, or WebP image."
            else:
                try:
                    image = Image.open(upload.stream)
                    image.verify()
                    upload.stream.seek(0)
                    UPLOAD_FOLDER.mkdir(parents=True, exist_ok=True)
                    upload.save(UPLOAD_FOLDER / filename)
                    return redirect(url_for("admin"))
                except (UnidentifiedImageError, OSError):
                    error = "File is not a valid image."
    return render_template("admin.html", gallery_images=gallery_images(), error=error)


if __name__ == "__main__":
    app.run(debug=True)