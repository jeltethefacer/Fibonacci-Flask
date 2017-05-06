from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

def fibonacci(amount):
    fib = [0,1]
    for x in range(amount -1):
        fib.append(fib[-1]+fib[-2])
    return fib[amount]

@app.route("/")
def index():
    return render_template("index.html", number=fibonacci(10))

if __name__ == "__main__":
    app.run(debug=True)
