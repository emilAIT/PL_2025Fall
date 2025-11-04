from collections import defaultdict
import csv
from datetime import date

def datediff(a, b):
    y1,m1,d1=[int(i) for i in a.split('-')]
    y2,m2,d2=[int(i) for i in b.split('-')]
    return (date(y2,m2,d2) - date(y1,m1,d1)).days

class Parking:
    def __init__(self, limit = 100):
        self.limit = limit
        self.d = defaultdict(dict)
        self.history = defaultdict(list)
        self.rate = 100
        self.blocked = set()

    def add_car(self, id, data='2025-11-04'):
        if id in self.d or id in self.blocked:
            return False
        self.d[id]["balance"]=0
        self.d[id]['start'] = data
        return True
    
    def add_balance(self, id, balance):
        if id not in self.d:
            return False
        self.d[id]['balance'] += balance
        return True
    
    def get_cost(self, id, data='2025-11-03'):
        if id not in self.d:
            return 0
        return datediff(self.d[id]['start'], data)*self.rate
    
    def remove_car(self, id, data='2025-11-03'):
        if id not in self.d:
            return False

        start = self.d[id]['start']
        end = data
        cost = self.get_cost(id, data)
        days = cost/self.rate


        self.history[id].append([start, end, cost, (days, id)]) 

        del self.d[id]
        return True

    def get_cars_count(self):
        return len(self.d)
    
    def has_car(self, id):
        return id in self.d
    
    def get_balance(self, id):
        return self.d.get(id, {"balance":0})['balance']

    def update_car_info(self, id, new_id):
        if id not in self.d or new_id in self.d:
            return False
        self.d[new_id] = self.d[id]
        del self.d[id]
    
    def block_car(self, id):
        self.blocked.add(id)
        return True
    

    def history_id(self, id, start, end):
        if id not in self.history:
            return []
        
        result = []
        for i in self.history[id]:
            s, e, _, _ = i
            if start <= s <= e <= end:
                result.append(i)
        return result


    def history_parking(self, start='2020-01-01', end='2025-12-31'):
        result = []
        for id in self.history:
            result += self.history_id(id, start, end)
        return result

    def get_available_parking_count(self):
        return self.limit - self.get_cars_count()
    
    def get_max_cost(self):
        arr = [i[2] for i in self.history_parking()]
        return max(arr)

    def get_min_cost(self):
        arr = [i[2] for i in self.history_parking()]
        return min(arr)

    def get_average(self):
        arr = [i[2] for i in self.history_parking()]
        return sum(arr)/len(arr)

    def get_top_n_by_check(self, n):
        arr = [(i[2], i[3][1]) for i in self.history_parking()]
        return sorted(arr)[-n:]

    def get_top_n_client(self, n):
        arr = []
        for key, value in self.history:
            s = sum(i[2] for i in value)
            arr.append((s, id))
        return sorted(arr)[-n:]

    def export_csv(self, filename):
        with open(filename, 'w') as fid:
            writer = csv.writer(fid)
            writer.writerow(['start', 'end','cost','(days, id)'])
            writer.writerows(self.history_parking('2020-01-01', '2025-12-31'))
