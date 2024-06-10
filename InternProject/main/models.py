from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Flavor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(200))

class Inventory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ingredient = db.Column(db.String(80), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

class Suggestion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    flavor = db.Column(db.String(80), nullable=False)
    allergies = db.Column(db.String(200))
