import os
from flask import Flask, render_template, send_from_directory, url_for
from forms import RegForm
from flask_uploads import UploadSet, IMAGES, configure_uploads
from quickRun import getFvAndShape


app = Flask(__name__)
app.config['SECRET_KEY'] = 'B3NzaC1ycDAQABAAABAQCkPsx7jEchCJDX'
app.config['UPLOADED_PHOTOS_DEST'] = 'uploads'

photos = UploadSet('photos',IMAGES)
configure_uploads(app,photos)


@app.route('/uploads/<filename>')
def get_file(filename):
    return send_from_directory(app.config['UPLOADED_PHOTOS_DEST'],filename)


@app.route('/register', methods=['GET','POST'])
def upload_image():
    form = RegForm()
    if form.validate_on_submit():
        filename = photos.save(form.earphoto.data)
        # print('upload/'+filename)
        ear = getFvAndShape('uploads/'+filename)
        ear_url = url_for('get_file',filename=filename)
    else:
        ear_url = None
        ear = None

    return render_template('registration.html',form=form, ear_url=ear_url, ear=ear)

if __name__ == '__main__':
    app.run(port=3000, debug=True)