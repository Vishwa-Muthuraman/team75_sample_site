from app import db
import datetime

class DATABASE_URL(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100), nullable=False)

    event = db.Column(db.String(100), nullable=False)

    hours = db.Column(db.Float(), nullable=False)

    stud_ID = db.Column(db.String(100), nullable=False)


    def __repr__(self):
        return f'{self.name} volunteered at {self.event} for {self.hours} hours. Student ID is {self.stud_ID}'
       
    def __init__(self, name, event, hours, stud_ID):
        self.name = name
        self.event = event
        self.hours = hours
        self.stud_ID = stud_ID

class Student_ID_Pairs(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100), nullable=False)

    stud_ID = db.Column(db.String(100), nullable=False)    
