from flask_sqlalchemy import SQLAlchemy
from _datetime import datetime

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

class Pet(db.Model):
    """Defines Pet table"""
    __tablename__ = "pets"

    def __repr__(self):
        return f"<Pet>"
    
    id = db.Column(db.Integer, 
                   primary_key=True, 
                   autoincrement=True)
    
    name = db.Column(db.Text,
                     nullable=False)
    
    species = db.Column(db.Text,
                        nullable=False)
    
    photo_url = db.Column(db.Text, default = 'https://pyxis.nymag.com/v1/imgs/0d8/a7e/a7e45af36625b8900e63c51d0ec925749c-over-the-garden-wall.rsquare.w700.jpg')

    age = db.Column(db.Integer)

    notes = db.Column(db.Text)

    available = db.Column(db.Boolean, nullable=False)