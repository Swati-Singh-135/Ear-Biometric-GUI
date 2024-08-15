from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FileField, IntegerField, validators, DateField, RadioField, SelectField
from flask_wtf.file import FileRequired, FileAllowed
from flask_uploads import UploadSet, IMAGES


photos = UploadSet('photos',IMAGES)


class RegForm(FlaskForm):
    earphoto = FileField(
        label="Ear Image",
        validators=[
            FileAllowed(photos,'Only images are allowed'),
            FileRequired('Ear Image Field should not be empty')
        ]
    )

    submit = SubmitField('Submit')
