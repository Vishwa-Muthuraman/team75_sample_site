from flask import Flask, request, jsonify, render_template

# configure app
app = Flask(__name__)
app.config["DEBUG"] = True
# connect to DBMS
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres@localhost/FIRST"

# instantiate DB
db = SQLAlchemy(app)
# Connect to engine
engine = create_engine("postgresql://postgres:postgres@localhost/FIRST")

@app.route('/index')
@app.route('/')
def index():
    return render_template("index.html")


if __name__ == '__main__':
    db.create_all() # - unsupress when we connect to RDBMS
    app.run(debug=True)