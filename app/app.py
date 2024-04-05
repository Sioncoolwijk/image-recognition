from flask import Flask, request, render_template, flash, send_from_directory, url_for
import os
from detect import fit_image

app = Flask(__name__)
app.secret_key = 'mysupersecretkey'

UPLOAD_FOLDER = os.path.join('static', 'uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':

        file = request.files.get('file')
        if file and file.filename:
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            url = '/'+filepath
            filepath = 'app/'+filepath
            file.save(filepath)
            return render_template('upload_form.html', file_url=url)
        else:
            flash('No file selected')
            return render_template('upload_form.html')
        
    return render_template('upload_form.html')

@app.route('/detect_image', methods=["POST"])
def detect_image():
    filename = request.form['filename']
    image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    name, prob = fit_image('app/'+image_path)
    return render_template('upload_form.html', name=name, prob=prob)

if __name__ == '__main__':
    app.run(debug=True)
