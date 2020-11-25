from app import db

class Volunteers(db.Model): # classes map to SQL Tables
    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100), nullable=False)

    event = db.Column(db.String(100), nullable=False)

    hours = db.Column(db.Float(), nullable=False)

    def __repr__(self):
        return f'{self.name} volunteered at {self.event} for {self.hours} hours'

    def __init__(self, name, event, hours):
        self.name = name
        self.event = event
        self.hours = hours


## table Volunteers
# columns: id, name, event, hours, FIRST_ID == Student IDs?
# -------------------------------
#           0, 'Matt', 'WISE', 2, 12345
#           1, 'Ian', 'FIRST', 3, 54321
#           2, 'Nihal', 'FIRST', 3, 09876
#           3, 'Matthew Smith', 'WISE', 2, 67890
#           4, 'Matthew Smith', 'WISE', 2, 11111



# date? StudentID?, recruit new people? mentors there?


# query Data
# Volunteers.query.('')


# TABLE: Volunteers
# columns: id, student_id, event, hours
# -------------------------------
#           0, 12345, 'WISE', 2
#           1, 11111, 'FIRST', 3
#           2, 22222, 'FIRST', 4
#           3, 12345, 'FIRST', 2


## table Users
# new user - when did they become a RoboRaider, age?, email, student ID

# columns: id, student_id, first_name, last_name, Email
#------------------------------------------------------
#           0, 12345, 'Matthew', 'Richtmyer', 'm;lasdf'
#           1, 11111, 'Ian',     'Golden', 'asdfasdf'
#           2, 22222, 'Nihal',   'Saxena', 'asdfasdfasdf'



# SQL ->

## table Super Users






## table Mentors
# 'Matt' - FIRST_ID = 12345

## table Sponsors
