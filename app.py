from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config["DEBUG"] = True

# # config app
# app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres@localhost/Students"
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir,'data.sqlite')


# # connect to SQLAlchemy
db = SQLAlchemy(app)

# # create engine
# engine = create_engine("postgresql://postgres:postgres@localhost/Students")


# And define table/class
class Student(db.Model):

    # manually chose what table name is. if we do not include, SQLAlchemy provides one
    __tablename__ = 'Students'

    # create database columns
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    graduation_year = db.Column(db.Integer)
    outreach_type = db.Column(db.Text)
    number_of_hours = db.Column(db.Integer)
    description = db.Column(db.Text)


    # define initializers
    def __init__(self, id, name, graduation_year, outreach_type, number_of_hours, description):
        self.id = id
        self.name = name
        self.graduation_year = graduation_year
        self.outreach_type = outreach_type
        self.number_of_hours = number_of_hours
        self.description = description

    # def __repr__(self):
    #     # define string representation of table
    #     return f"Student {self.name} is {self.age} year/s old"
# let's do this by Friday August 28


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/Good_Standing")
def Good_Standing():
    return render_template("Good_Standing.html")

@app.route("/about_us")
def about_us():
    return render_template("about_us.html")

@app.route("/hours")
def hours():
    return render_template("hours.html")

@app.route("/View_Hours")
def View_hours():
    return render_template("View_Hours.html")

@app.route("/User_View")
def User_View():
    return render_template("User_View.html")

@app.route("/manasi")
def manasi():
    return render_template("manasi.html")

@app.route("/ian")
def ian(): 
    return render_template("ian.html")

@app.route("/nihal")
def nihal():
    return render_template("nihal.html")

if __name__ == '__main__':
    #db.create_all() # - unsupress when we connect to RDBMS
    app.run(debug=True)