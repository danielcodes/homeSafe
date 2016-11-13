
from flask import Flask, jsonify, request
from regression import findWidth
import numpy as np
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/getwidth')
def getWidth():
    values = findWidth(int(request.args.get('speed')))
    values = values.tolist()
    res = values[0][0]
    res = round(res, 2)

    return jsonify(width=res)

if __name__ == "__main__":
    app.run()


