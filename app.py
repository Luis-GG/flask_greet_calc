# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)


@app.route("/add")
def my_add():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    return f"{a + b}"

@app.route("/sub")
def my_sub():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    return f"{a - b}"
    
@app.route("/mult")
def my_mult():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    return f"{a * b}"

@app.route("/div")
def my_div():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    return f"{a / b}"






operations = {
    "add": add,
    "sub": sub,
    "mult": mult,
    "div": div
}

@app.route("/math/<oper>")
def all_math(oper):
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))

    result = operations[oper](a,b)

    return str(result)

