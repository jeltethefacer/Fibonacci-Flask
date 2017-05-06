from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import Required

app = Flask(__name__)
app.config["SECRET_KEY"] = "dit raad je toch nooit in jouw missearbele leven"

bootstrap = Bootstrap(app)



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
    number = 0
    if form.validate_on_submit():
        number = fibonacci(form.number.data)
        form.number.data = None
    return render_template("index.html", number=number, form=form)

if __name__ == "__main__":
    app.run(debug=True)
