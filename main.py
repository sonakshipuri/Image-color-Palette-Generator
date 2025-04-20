from flask import Flask, render_template, request, url_for, flash, redirect, send_from_directory
from PIL import Image
import colorfinder
import os
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
PLOT_FOLDER = 'static/plots'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        if 'image' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['image']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            try:
                os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
                file.save(filepath)
                img = Image.open(filepath)
                print(f"Image mode after opening: {img.mode}")
                plot_filename_base = f"palette_kmeans_{secure_filename(file.filename)}"
                plot_filename = f"{plot_filename_base}.png"
                colorfinder.get_colors_kmeans(img, filename=plot_filename)
                return render_template("index.html", uploaded_filename=filename, plot_filename=plot_filename)
            except Exception as e:
                return render_template("index.html", error=str(e))
    return render_template("index.html")

@app.route('/uploads/<filename>')
def display_image(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/static/plots/<filename>')
def display_plot(filename):
    return send_from_directory('static/plots', filename)

if __name__ == "__main__":
    app.run(debug=True, port=5001)