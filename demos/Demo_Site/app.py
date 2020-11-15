from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'my_secret_key_12345'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///volunteers.db'

db = SQLAlchemy(app)

from routes import *

if __name__ == '__main__':
    app.run(debug=True)
