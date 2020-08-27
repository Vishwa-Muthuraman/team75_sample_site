import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# Steps: 
# Create Flask App
# Configure Flask App for SQLAlchemy
# Pass app into SQLAlchemy class calls

# Create data model in Flask - this will link to a
# table in a SQL database. Python does this for us
# to abstract the SQL

# Then can perform CRUD operations


basedir = os.path.abspath(os.path.dirname(__file__))
# __file__ --> whatever the file name is (e.g. app.py)
# abspath --> grabs full filepath for this file
# provides right dir independent of OS

# create flask app
app = Flask(__name__)

# set up SQL database
# first connect to database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir,'data.sqlite')
# do not track modifications - can change this later
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# create database
db = SQLAlchemy(app)


#########################################
# create first model

# classes create table in database
class Student(db.Model):

    # manually chose what table name is. if we do not include, SQLAlchemy provides one
    __tablename__ = 'Students'

    # create serial primary key
    id = db.Column(db.Integer, primary_key=True)
    # add name column
    name = db.Column(db.Text)
    # add age column
    age = db.Column(db.Integer)

    # define initializers
    def __init__(self, name, age):
        # note id autocreated
        self.name = name
        self.age = age

    def __repr__(self):
        # define string representation of table
        return f"Student {self.name} is {self.age} year/s old"


# class Hours(db.Model):
#     # fill in columns you want and initialize them in the __init__
    
#     # s_fk = pull FK from Students (s_id)

#     # id => primary key for Hours table

#     # event db.Column(db.Text)
#     # hours db.Column(db.Integer) -> data types, how are the numbers coming in from UI??


    
    
#     def __init__(self):
#         #asdf
    


# Hours(student_FK, hours, event...)





# Pseudo Code


# Question: should we make two databases for students to access and for mentors to access?
# 
# Ans: 1 database - and we should restrict access somehow (either by private methods or by
# security). BECAUSE - if you follow this logic, it wouldn't be 2 databases it would be n databases


# class Mentor(db.Model):

#     # create serial primary key
#     id = db.Column(db.Integer, primary_key=True)
#     # add name column
#     name = db.Column(db.Text)
#     # add age column
#     age = db.Column(db.Integer)

#     # define initializers
#     def __init__(self, name, age):
#         # note id autocreated
#         self.name = name
#         self.age = age


#     def access_all_students():
#         # function to query all students


# class Student(db.Model):

#     # create serial primary key
#     id = db.Column(db.Integer, primary_key=True)
#     # add name column
#     name = db.Column(db.Text)
#     # add age column
#     age = db.Column(db.Integer)

#     # define initializers
#     def __init__(self, name, age):
#         # note id autocreated
#         self.name = name
#         self.age = age


#     def access_my_scores():
#         # function to query only this students




# Question: what would the headings look like? 
# Visualize the table
# Two tables: 

# Table 1: Students
# PK, Name, Metadata you want.. 
# 0, 'John Smith'
# 1, 'Ian'
# 2, 'Nihal', 
# 3, 'John Smith' .... 


# Table 2: Hours
# PK, FK, Event_Name, Hours, Location, Date
# 0, 1, 'WISE', 2, 'HHS', July 15, 2020
# 1, 0, 'WiSTEM2D', 3, 'JNJ', July 10, 2020
# 2, 3, 'Farmbot', 6, 'HHS', Aug 20, 2020
# 3, 3, 'Wise', 2, 'JNJ', Aug 10, 2020

# Query - 
# db.Session.query.get(3) -> both rows 2 and 3. now would have to aggregate data accordingly



# TO DOs
# 1. Design: what info (data??) do we need?? Week of July 24
    # a. Need to have UI for it
    # b. Need to create Class with that data

# 2. Start piping data together Week of Mid Aug for first stab? 3 ish weeks
    # a. Pass data from HTML to python
    # b. Pass data from Python to DBMS
    # c. Create query to aggregate data from DBMS
        # i. Functionalize this!! def getHours(userId): return sum of hours
    # d. Serve up data to HTML