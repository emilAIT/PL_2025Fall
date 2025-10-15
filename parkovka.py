from flask import Flask, request
app = Flask(__name__)

from collections import defaultdict
from time import time

d = defaultdict(int)
cars_enter = defaultdict(list)
cars_paid = defaultdict(list)

rate = 3
history = []

@app.route('/zaezd')
def isikender():
    id = request.args.get("id")
    d[id] = time()
    history.append(f'{time()} zaezd {id}')
    cars_enter[id].append(time())
    return f'welcome to the garaj {id}'

def mymin(arr):
    return min(arr)

@app.route('/skolko')
def skolko():
    id = request.args.get("id")
    now = time()
    total = int( (now - d[id]) ) * rate
    history.append(f'{time()} zapros skolko na {id}')
    # mymin(arr)
    return f'Total summa : {total}'

@app.route('/platej')
def platej():
    id = request.args.get("id")
    summa = int(request.args.get("summa"))
    d[id] += summa/rate
    history.append(f'{time()} platej za {id} na {summa} summu')
    cars_paid[id].append(time())
    return f'spasibo za platej na summu {summa}'


@app.route('/ispaid')
def is_paid():
    id = request.args.get("id")
    if d[id] > time() -  15:
        del d[id]
        history.append(f'{time()} viezd {id}')
        return f'thanks for using garage'
    else:
        history.append(f'{time()} viezd {id} unsuccessful')
        return f'dude, pay first'
    
app.run()