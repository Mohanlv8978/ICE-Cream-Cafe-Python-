from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

from models import db, Flavor, Inventory, Suggestion

db.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/flavors', methods=['GET', 'POST'])
def flavors():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        new_flavor = Flavor(name=name, description=description)
        db.session.add(new_flavor)
        db.session.commit()
        return redirect(url_for('flavors'))
    seasonal_flavors = Flavor.query.all()
    return render_template('flavors.html', flavors=seasonal_flavors)

@app.route('/inventory', methods=['GET', 'POST'])
def inventory():
    if request.method == 'POST':
        ingredient = request.form['ingredient']
        quantity = request.form['quantity']
        new_ingredient = Inventory(ingredient=ingredient, quantity=quantity)
        db.session.add(new_ingredient)
        db.session.commit()
        return redirect(url_for('inventory'))
    ingredients = Inventory.query.all()
    return render_template('inventory.html', inventory=ingredients)

@app.route('/suggestions', methods=['GET', 'POST'])
def suggestions():
    if request.method == 'POST':
        flavor = request.form['flavor']
        allergies = request.form['allergies']
        new_suggestion = Suggestion(flavor=flavor, allergies=allergies)
        db.session.add(new_suggestion)
        db.session.commit()
        return redirect(url_for('suggestions'))
    return render_template('suggestions.html')

@app.route('/Cart', methods=['GET', 'POST'])
def cart():
    if request.method == 'POST':
        flavor_id = request.form['flavor_id']
        ingredient_id = request.form['ingredient_id']
        suggestion_id = request.form['suggestion_id']
        flavor = Flavor.query.get(flavor_id)
        ingredient = Inventory.query.get(ingredient_id)
        suggestion = Suggestion.query.get(suggestion_id)
        cart_items = [flavor, ingredient, suggestion]
        return render_template('cart.html', cart_items=cart_items)
    flavors = Flavor.query.all()
    ingredients = Inventory.query.all()
    suggestions = Suggestion.query.all()
    return render_template('cart.html', flavors=flavors, ingredients=ingredients, suggestions=suggestions)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
