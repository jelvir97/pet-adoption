from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, RadioField,IntegerField
from wtforms.validators import InputRequired, NumberRange, Optional, URL

class AddPet(FlaskForm):
    """Form for adding/editing pet"""
    name = StringField("Pet Name",validators=[InputRequired(message="Please enter a name")])
    species = RadioField("Species",validators=[InputRequired(message="Please choose a species")],choices=[('cat','cat'),('dog','dog'),('porcupine','porcupine')])
    photo_url = StringField("Image Address", validators = [Optional(),URL(message="Please enter valid URL")])
    age =IntegerField("Age",validators=[Optional(),NumberRange(min=0, max=30, message="Age must be between 0 and 30")])
    notes = StringField("Additional Notes")
    available = BooleanField('Available for Adoption')

    