from collections import defaultdict

class Item:
    def __init__(self, shtrihkod, name, purchase_price, sale_price):
        self.name = name
        self.purchase_price = purchase_price
        self.sale_price = sale_price
        self.shtrihkod = shtrihkod 
    
    def set_price(self, price):
        self.sale_price = price

class Client:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

class Store:
    def __init__(self, store_name):
        self.store_name = store_name
        self.items = defaultdict(int)
        self.names = {}
        self.history = []
        self.cart = defaultdict(list)
        self.sold_items = defaultdict(int)
        self.clients = []
        self.item_objects = []

    def add_product(self, item:Item, count):
        self.items[item.shtrihkod] += count
        self.names[item.shtrihkod] = item 

    def add_to_client_cart(self, client:Client, item:Item, count):
        if count <= self.items[item.shtrihkod]:
            self.cart[client.phone].append( (item.shtrihkod, count) )
            self.items[item.shtrihkod] -= count
            self.sold_items[item.shtrihkod] += count
    
    def close_cart(self, client):
        total = 0 
        for shtrihkod, count in self.cart[client.phone]:
            total += self.names[shtrihkod].sale_price * count
        del self.cart[client.phone]
        self.history.append((client.phone, total))

    def show_history(self):
        result = ''
        for client, total in self.history:
            result += f'{client}: {total}\n'
        result += '\n'
        return result

    def show_popular_items(self, n = 5):
        result = ''
        top = sorted(self.sold_items.items(), key = lambda x:x[1])[-n:]
        for shtrihcode, count in top:
            result += f'{count}, {shtrihcode}, {self.names[shtrihcode].name}, {self.names[shtrihcode].sale_price} \n'
        result += '\n\n'
        return result

    def show_profit(self):
        profit = 0
        for shtrihkod, count in self.sold_items.items():
            item = self.names[shtrihkod]
            profit += (item.sale_price - item.purchase_price) * count
        return profit

    def update_price(self, item, new_price):
        self.names[item.shtrihkod].set_price(new_price)

    def count_clients(self):
        return len(set([phone for phone, total in self.history]))

    def show_item(self, item: Item):
        result = f'name: {item.name}\nshtrihkod: {item.shtrihkod}\nsale_price: {item.sale_price}\npurchase_price: {item.purchase_price}\n'
        result += f'sold items: {self.sold_items[item.shtrihkod]}\n'
        return result