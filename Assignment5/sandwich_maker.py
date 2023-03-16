import sqlalchemy
from flask import Flask, flash, redirect, url_for, render_template, session
from flask import request

from flask_sqlalchemy import SQLAlchemy

DB_HOST = "localhost"
DB_NAME = "sandwich_maker"
DB_USERNAME = "root"
DB_Password = "Leenababy8*"

database_file = f"mysql+pymysql://{DB_USERNAME}:{DB_Password}@{DB_HOST}:3306/{DB_NAME}"

app = Flask(__name__)
app.secret_key = "mysecret"
app.config["SQLALCHEMY_DATABASE_URI"] = database_file

db = SQLAlchemy(app)

if __name__ == '__main__':
    app.run(port=3306, host="localhost", debug=True)


class Resource(db.Model):
    __tablename__ = 'resources'
    id = db.Column(db.Integer, primary_key=True)
    item = db.Column(db.String(100), nullable=False)
    amount = db.Column(db.Integer, nullable=False)

    def __init__(self, item, amount):
        self.item = item
        self.amount = amount


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/resource")
def resource():
    return render_template("resources/list.html", resources=Resource.query.all())


@app.route('/addresource', methods=['GET', 'POST'])
def add_resource():
    if request.method == 'POST':
        if not request.form['item'] or not request.form['amount']:
            flash('Please enter all the fields', 'error')
        else:
            resource = Resource(request.form['item'], request.form['amount'])

            db.session.add(resource)
            db.session.commit()

            flash('Record was successfully added')
            return redirect(url_for('resource'))
    return render_template('resources/add.html')


@app.route('/updateresource/<int:id>/', methods=['GET', 'POST'])
def update_resource(id):
    if request.method == 'POST':
        if not request.form['item'] or not request.form['amount']:
            flash('Please enter all the fields', 'error')
        else:
            resource = Resource.query.filter_by(id=id).first()
            resource.item = request.form['item']
            resource.amount = request.form['amount']
            db.session.commit()

            flash('Record was successfully updated')
            return redirect(url_for('resource'))
    data = Resource.query.filter_by(id=id).first()
    return render_template("resources/update.html", data=data)


@app.route('/deleteresource/<int:id>/', methods=['GET', 'POST'])
def delete_resource(id):
    if request.method == 'POST':
        resource = Resource.query.filter_by(id=id).first()
        db.session.delete(resource)
        db.session.commit()

        flash('Record was successfully deleted')
        return redirect(url_for('resource'))
    data = Resource.query.filter_by(id=id).first()
    return render_template("resources/delete.html", data=data)


class Sandwich(db.Model):
    __tablename__ = 'sandwich'
    id = db.Column(db.Integer, primary_key=True)
    item = db.Column(db.String(100), nullable=False)
    amount = db.Column(db.Integer, nullable=False)

    def __init__(self, item, amount):
        self.item = item
        self.amount = amount


@app.route("/sandwich")
def sandwich():
    return render_template("sandwich/list.html", sandwich=Sandwich.query.all())


@app.route('/addsandwich', methods=['GET','POST'])
def add_sandwich():
    if request.method == 'POST':
        if not request.form['item'] or not request.form['amount']:
            flash('Please enter all the fields', 'error')
        else:
            sandwich = Sandwich(request.form['item'], request.form['amount'])

            db.session.add(sandwich)
            db.session.commit()

            flash('Record was successfully added')
            return redirect(url_for('sandwich'))
    return render_template('sandwich/add.html')


@app.route('/updatesandich/<int:id>/', methods=['GET','POST'])
def update_sandwich(id):
    if request.method == 'POST':
        if not request.form['item'] or not request.form['amount']:
            flash('Please enter all the fields', 'error')
        else:
            sandwich = Sandwich.query.filter_by(id=id).first()
            sandwich.item = request.form['item']
            sandwich.amount = request.form['amount']
            db.session.commit()

            flash('Record was successfully updated')
            return redirect(url_for('sandwich'))
    data = Sandwich.query.filter_by(id=id).first()
    return render_template("sandwich/update.html", data=data)


@app.route('/deletesandwich/<int:id>', methods=['GET','POST'])
def delete_sandwich(id):
    if request.method == 'POST':
        sandwich = Sandwich.query.filter_by(id=id).first()
        db.session.delete(sandwich)
        db.session.commit()

        flash('Record was successfully deleted')
        return redirect(url_for('sandwich'))
    data = Sandwich.query.filter_by(id=id).first()
    return render_template("sandwich/delete.html", data=data)
