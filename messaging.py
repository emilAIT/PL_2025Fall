from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from collections import defaultdict
from datetime import datetime
import pomosh

app = Flask(__name__)
CORS(app)

d = defaultdict(list)

@app.route("/")
def glavniy():
    return render_template("ait.html")

@app.route("/send")
def pochta():
    kto = request.args.get("kto", "")
    komu = request.args.get("komu","")
    chto = request.args.get("chto","")
    vremya = datetime.now().strftime("%m/%d/%Y - %H:%M:%S")

    info = f'{vremya} : {kto} - {komu} -> {chto}'

    d[kto].append(info)
    d[komu].append(info)

    result = ""
    for i in d[kto]:
        result += i + "<br>"
    return jsonify({'otvet': result})

@app.route('/kto')
def kto():
    kto = request.args.get("kto", "")
    result = ""
    for i in d[kto]:
        result += i + "<br>"
    return jsonify({'otvet': result})

@app.route('/mymin')
def pomosh_min():
    kto = request.args.get("kto", "")
    return pomosh.mymin(d[kto])

@app.route('/vse')
def allmessages():
    result = ""
    for k, v in d.items():
        for i in v:
            result += i + "<br>"
    return jsonify({'otvet': result})

