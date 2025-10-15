from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

d = {
    "0001": {"item": "sneakers", "price": 80},
    "0002": {"item": "cola", "price": 120},
    "0003": {"item": "bread borodinskiy", "price": 60}
}


counter = {"count": 0}

@app.route("/ait")
def lookup():
    counter["count"] += 1
    shtrihcode = request.args.get("shtrihcode")
    item = d.get(shtrihcode, None)
    try:
        name = item["item"]
        price = item["price"]
        return f'{shtrihcode} : {name} -> {price}'
    except:
        return f'item with {shtrihcode} not found'

@app.route("/ait2")
def lookup2():
    counter["count"] += 1
    
    shtrihcodes = request.args.get("shtrihcodes").split(",")
    result = ""
    for shtrihcode in shtrihcodes:
        item = d.get(shtrihcode, None)
        name = item["item"]
        price = item["price"]
        result += f'{shtrihcode} : {name} -> {price}<br>'
    return result

@app.route('/kancha')
def count_jonot():
    return str(counter)

if __name__ == "__main__":
    app.run()
