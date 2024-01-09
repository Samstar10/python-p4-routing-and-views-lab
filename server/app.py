#!/usr/bin/env python3

from flask import Flask


app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(parameter)
    return parameter

@app.route('/count/<int:number>')
def count(number):
    result = '\n'.join(str(i) for i in range(number))
    return result

@app.route('/math/<float:num1>/<string:operation>/<float:num2>')
def math(num1, num2, operation):
    num1 = float(num1)
    num2 = float(num2)
    if operation == '+':
        return str(num1 + num2)
    elif operation == '-':
        return str(num1 - num2)
    elif operation == '*':
        return str(num1 * num2)
    elif operation == 'div':
        return str(num1 / num2)
    elif operation == '%':
        return str(num1 % num2)

if __name__ == '__main__':
    app.run(port=5555, debug=True)