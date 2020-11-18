from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
# app.config["DEBUG"] = True
app.config['SECRET_KEY'] = 'my_secret_key_12345'
# # # config app
# app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres@localhost/Students"
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir,'EventRegist.db')

# # connect to SQLAlchemy
db = SQLAlchemy(app)


# # create engine
# engine = create_engine("postgresql://postgres:postgres@localhost/Students")


# And define table/class
# class Student(db.Model):

#     # manually chose what table name is. if we do not include, SQLAlchemy provides one
#     __tablename__ = 'Students'

#     # create database columns
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.Text)
#     graduation_year = db.Column(db.Integer)
#     outreach_type = db.Column(db.Text)
#     number_of_hours = db.Column(db.Integer)
#     description = db.Column(db.Text)


#     # define initializers
#     def __init__(self, id, name, graduation_year, outreach_type, number_of_hours, description):
#         self.id = id
#         self.name = name
#         self.graduation_year = graduation_year
#         self.outreach_type = outreach_type
#         self.number_of_hours = number_of_hours
#         self.description = description

    # def __repr__(self):
    #     # define string representation of table
    #     return f"Student {self.name} is {self.age} year/s old"
# let's do this by Friday August 28

from routes import *

if __name__ == '__main__':
    #db.create_all() # - unsupress when we connect to RDBMS
    app.run(debug=True)