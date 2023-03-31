from flask import Flask, request
from pydantic import BaseModel


app = Flask(__name__)

class Numbers(BaseModel):
    num1: float
    num2: float

@app.route('/addition', methods=['POST'])
def addition():
    numbers = Numbers(**request.json)
    result = numbers.num1 + numbers.num2
    return {"result": result}

@app.route('/multiplication', methods=['POST'])
def multiplication():
    numbers = Numbers(**request.json)
    result = numbers.num1 * numbers.num2
    return {"result": result}

@app.route('/subtraction', methods=['POST'])
def subtraction():
    numbers = Numbers(**request.json)
    result = numbers.num1 - numbers.num2
    return {"result": result}

if __name__ == '__main__':
    app.run(debug=True)
