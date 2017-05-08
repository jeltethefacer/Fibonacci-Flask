from flask import Flask, render_template, redirect, url_for, session
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from wtforms import IntegerField, SubmitField
from wtforms.validators import Required
import os
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config["SECRET_KEY"] = "dit raad je toch nooit in jouw missearbele leven"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir, 'temp.sqlite')
app.config["SQLALCHEMY_COMMIT_ON_TEARDOWN"] = True
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

bootstrap = Bootstrap(app)
db = SQLAlchemy(app)
manager = Manager(app)

class Numbers(db.Model):
    __tablename__ = "Numbers"
    id = db.Column(db.Integer, primary_key = True)
    number = db.Column(db.Integer)

    def __repr__(self):
        return "<Number: %i>" % self.number

class NumberForm(FlaskForm):
    number = IntegerField("Which fibonacci number?", validators=[Required()])
    submit = SubmitField("Submit")

def fibonacci(amount):
    fib = [0,1]
    for x in range(amount -1):
        fib.append(fib[-1]+fib[-2])
    return fib[amount]



@app.route("/", methods=["GET", "POST"])
def index():
    form = NumberForm()
    if form.validate_on_submit():
        session["number"] = fibonacci(form.number.data)
        number = Numbers(number = form.number.data)
        #print(Numbers.query.all()) you can use it for debugging the db
        db.session.add(number)
        return redirect(url_for("index"))
    return render_template("index.html", number=session.get("number"), form=form, database=Numbers.query.all())

if __name__ == "__main__":
    manager.run()
