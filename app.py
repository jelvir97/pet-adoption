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

@app.route('/add', methods=["GET","POST"])
def add_new_pet():
    """Renders add pet form and Handles POST request"""
    form = AddPet()
    
    if(form.validate_on_submit()):
        name = form.name.data
        species = form.species.data
        age = form.age.data if form.age.data else None
        notes = form.notes.data if form.notes.data else None
        photo_url = form.photo_url.data if form.photo_url.data else None
        available = form.available.data

        pet = Pet(name=name,species=species,age=age,notes=notes,photo_url=photo_url,available=available)

        db.session.add(pet)
        db.session.commit()

        return redirect('/')
    else:
        
        return render_template('add_pet.html',form=form)
    
@app.route('/<id>/edit',methods=['GET','POST'])
def edit_pet(id):
    """Renders edit form and handles edit POST request."""
    pet = Pet.query.get(int(id))
    form = AddPet(obj=pet)

    if(form.validate_on_submit()):

        pet.name = form.name.data
        pet.species = form.species.data
        pet.age = form.age.data 
        pet.notes = form.notes.data if form.notes.data else None
        pet.photo_url = form.photo_url.data if form.photo_url.data else None
        pet.available = form.available.data

        db.session.add(pet)
        db.session.commit()

        flash(f"Pet info updated succesfully!")
        return redirect(f'/{id}/edit')
    else:
        return render_template('update_pet.html',form=form)
