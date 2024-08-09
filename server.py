from flask import Flask, render_template, request
from maths.mathematics import subtraction, summation, multiplication
import os

app = Flask(__name__)


@app.route("/sum")
def sum_route():
    num1 = float(request.args.get('num1'))
    num2 = float(request.args.get('num2'))
    result = summation(num1, num2)
    return str(result)


@app.route("/sub")
def sub_route():
    num1 = float(request.args.get('num1'))
    num2 = float(request.args.get('num2'))
    result = subtraction(num1, num2)
    return str(result)


@app.route("/mul")
def mul_route():
    num1 = float(request.args.get('num1'))
    num2 = float(request.args.get('num2'))
    result = multiplication(num1, num2)
    return str(result)


@app.route('/')
def home():
    print("Current working directory:", os.getcwd())  # Debug line
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)