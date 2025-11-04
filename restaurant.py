from flask import Flask, request
from flask_cors import CORS
from collections import defaultdict
app = Flask(__name__)
CORS(app)

def get_params(key1, key2=None, key3=None):
    data = request.args
    param1 = data.get(key1)
    param2, param3 = None, None
    if key2:
        param2 = data.get(key2)
    if key3:
        param3 = data.get(key3)
    return param1, param2, param3

def check(condition):
    if condition:
        return True
    else:
        raise ValueError('Invalid')



admin_password = 'ait'

menu = defaultdict(int)
tables = defaultdict(int)
orders = defaultdict(lambda: defaultdict(int))

@app.route('/add')
def add_to_menu():
    admin, name, price = get_params('admin', 'name', 'price')
    price = int(price)
#    try:
    if check(admin==admin_password) or check(name not in menu) or check(price > 0):
        menu[name] = price                           ###
    return 'Successfully added to menu'
#    except:
#        return 'Invalid request'

@app.route('/delete_item')
def delete_item():
    admin, name, _ = get_params('admin', 'name')
    try:
        if check(admin==admin_password) or check(name in menu):
            del menu[name]                                          ####
        return 'Successfully deleted item'
    except:
        return 'Invalid request'
    
@app.route('/update_price')
def update_price():
    admin, name, price = get_params('admin', 'name', 'price')
    price = int(price)
    try:
        if check(admin==admin_password) or check(name in menu) or check(price>0):
            menu[name] = price                              ###
        return 'Successfully updated items price'
    except:
        return 'Invalid request'


@app.route('/get_menu')
def get_menu():
    return str(menu)

@app.route('/add_table')
def add_table():
    admin, table, seats = get_params('admin', 'table', 'seats')
    seats = int(seats)
    try:
        if check(admin==admin_password) or check(table not in tables) or check(seats>0):
            tables[table] = seats                              #######
        return 'Successfully deleted item'
    except:
        return 'Invalid request'

@app.route('/total_seats')
def total_seats():
    return str(sum(tables.values()))

@app.route('/add_to_order')
def add_to_order():
    table, item, qty = get_params('table', 'item', 'qty')
    qty = int(qty)
    try:
        if check(table in tables) or check(item in menu):
            orders[table][item] += qty                      #####
        return 'Successfully added item to order'
    except:
        return 'Invalid request'
    

@app.route('/order_view')
def order_view():
    table, _, _ = get_params('table')
    try:
        if check(table in tables):
            result = ''
            total = 0
            for item, qty in orders[table].items():
                result += f'{item}\t{qty}\t{qty*menu[item]}<br>'
                total += qty*menu[item]
            result += f'Total: {total}'
        return result
    except:
        return 'Invalid request'
    
@app.route('/close_order')
def close_order():
    table, _, _ = get_params('table')
    try:
        if check(table in tables):
            del orders[table]                       #####
        return 'Successfully closed order'
    except:
        return 'Invalid request'


app.run()