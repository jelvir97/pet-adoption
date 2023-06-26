from flask_wtf import FlaskForm
from wtforms import StringField, FloatField
from wtforms.validators import InputRequired

class AddPet(FlaskForm):
    name = StringField("Pet Name",validators=[InputRequired()])
    species = StringField("Species",validators=[InputRequired()])
    photo_url = StringField("Image Address")
    age =StringField("Age")
    notes = StringField("Additional Notes")

    