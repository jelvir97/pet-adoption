from flask import Flask, request,render_template, redirect,flash,session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from sqlalchemy import Text, text
from forms import AddPet

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pet_adoption'
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'woohoo!123'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

app.app_context().push()
connect_db(app)

@app.route('/')
def hi():
    pets = Pet.query.all()
    return render_template('home.html', pets=pets)

@app.route('/pets/new')
def new_pet():
    form = AddPet()
    return render_template('add_pet.html',form=form)