from flask import Flask, request
from flask_cors import CORS
from collections import defaultdict
import csv
app = Flask(__name__)
CORS(app)


d = defaultdict(lambda: defaultdict(list))
users = defaultdict(str)

with open('ait25PL.csv') as fid:
    reader = list(csv.reader(fid))
    for i in reader:
        name = i[0].replace(' ', '')
        for x, j in enumerate(i[1:]):
            try:
                grade = int(j)
                d[name]['PL'].append((x, grade))
            except:
                d[name]['PL'].append( (x, grade))
        users[name] = '123'

print(users.keys())

admin_password = 'ait'

# /add_student?admin=ADMIN&username=U&password=P
@app.route('/add_student')
def add_student():
    data = request.args
    admin = data.get('admin', None)
    student_name = data.get('username', None)
    student_password = data.get('password', None)

    if admin != admin_password:
        return 'incorrect request'
    
    if student_name in users.keys():
        return 'incorrect request'
    
    users[student_name] = student_password
    return 'successfully added student'


#/add_grade?admin=ADMIN&username=U&course=C&item=I&grade=G
@app.route('/add_grade')
def add_grade():
    data = request.args
    admin = data.get('admin')
    student_name = data.get('username')
    course = data.get('course')
    item = data.get('item')
    grade = int(data.get('grade'))
    
    if admin_password != admin or student_name not in users:
        return 'invalid request'

    d[student_name][course].append((item, grade))
    return 'successfully added student grade'

#/grades?username=U&password=P
@app.route('/grades')
def grades():
    data = request.args
    student_name = data.get('username')
    student_password = data.get('password')

    if student_name not in users or users[student_name] != student_password:
        return 'invalid request'
    
    grades = d[student_name]
    result = []
    for course_name, list_of_grades in grades.items():
        s = sum([i[1] for i in list_of_grades])
        result.append( (course_name, s/len(list_of_grades)) )
    
    return str(result)


# /change_password?username=U&old=OLD&new=NEW
@app.route('/change_password')
def change_password():
    data = request.args
    username = data.get('username')
    old = data.get('old')
    new = data.get('new')

    if username not in users or old != users[username]:
        return 'invalid request' 

    users[username] = new

    return 'successfully changed the password'


#/count_students?admin=ADMIN → количество пользователей.
@app.route('/count_students')
def count_students():
    admin = request.args.get('admin')
    if admin != admin_password:
        return 'invalid request'
    
    return str({'student count': len(d)})


#/delete_student?admin=ADMIN&username=U&password=P
@app.route('/delete_student')
def delete_student():
    data = request.args
    admin = data.get('admin', None)
    student_name = data.get('username', None)
    student_password = data.get('password', None)

    if admin != admin_password:
        return 'incorrect request'
    
    if student_name not in users.keys():
        return 'incorrect request'
    
    del users[student_name]
    del d[student_name]

    return 'successfully removed student'

#/list_students?admin=ADMIN → массив имён, отсортированный.
@app.route('/list_students')
def list_students():
    admin = request.args.get('admin')
    if admin != admin_password:
        return 'invalid request'
    
    return str(sorted(users.keys()))

#/letter_grade?username=U&password=P
@app.route('/letter_grade')
def letter_grade():
    data = request.args
    username = data.get('username')
    password = data.get('password')

    if username not in users or password != users[username]:
        return 'invalid request' 

    grades = d[username]
    result = []
    for course_name, list_of_grades in grades.items():
        avg = sum([i[1] for i in list_of_grades])/len(list_of_grades)
        if avg >= 90:
            result.append((course_name, 'A'))
        elif avg >= 80:
            result.append((course_name, 'B'))  
        elif avg >= 70:
            result.append((course_name, 'C'))
        elif avg >= 60:
            result.append((course_name, 'D'))

    return str(result)


#/delete_grade?admin=ADMIN&username=U&course=C&item=I
@app.route('/delete_grade')
def delete_grade():
    data = request.args
    admin = data.get('admin')
    student_name = data.get('username')
    course = data.get('course')
    item = data.get('item')
    
    if admin_password != admin or student_name not in users:
        return 'invalid request'

    for j, i in enumerate(d[student_name][course]):
        if i[0] == item:
            d[student_name][course].pop(j)
            return 'successfully removed student grade'
    
    return 'could not delete student grade'


# /exists?username=U 
@app.route('/exists')
def exists():
    data = request.args
    username = data.get('username')
    if username in users:
        return str({'exists': True})
    else:
        return str({'exists': False})
    

app.run()