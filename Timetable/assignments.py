from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import datetime

timetable = Flask(__name__)
timetable.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/schedule'
db = SQLAlchemy(timetable)

class Timetable(db.Model):
    name= db.Column(db.String,nullable=False)
    course= db.Column(db.String,nullable=False)
    scheduleTask= db.Column(db.String,nullable=False)
    date= db.Column(db.Date,nullable=False)
    regno= db.Column(db.Integer, primary_key=True)
    

@timetable.route('/add', methods=['POST', 'GET'])
def Contact():
    if(request.method == 'POST'):
        
        name= request.form.get('name')
        course = request.form.get('course')
        scheduleTask = request.form.get('schedule')
        date = request.form.get('date')
        regno = request.form.get('reg')

        entry = Timetable(name=name, course=course, scheduleTask=scheduleTask, date=date, regno=regno)
        db.session.add(entry)
        db.session.commit()
    


    return render_template("form.html")


class signup(db.Model):
    usname= db.Column(db.String(50),nullable=False)
    password= db.Column(db.Integer,primary_key=True)




@timetable.route("/")
def index():
    return render_template("index.html")

@timetable.route('/register', methods=['POST', 'GET'])
def register():
    if(request.method == 'POST'):
        usname= request.form.get('usname')
        password = request.form.get('password')
        entry1 = signup(usname=usname, password=password)
        db.session.add(entry1)
        db.session.commit()
    return render_template("register.html")

@timetable.route("/schedule")
def show():
    tabeldata = Timetable.query.all()
    return render_template("schedule.html", Timetable=tabeldata)
    


timetable.run(debug=True)

