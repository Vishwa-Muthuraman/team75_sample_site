from flask import Flask, request, jsonify, render_template

app = Flask(__name__)
app.config["DEBUG"] = True

# # config app
# app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres@localhost/__NAME-HERE__"

# # connect to SQLAlchemy
# db = SQLAlchemy(app)

# # create engine
# engine = create_engine("postgresql://postgres:postgres@localhost/__NAME-HERE__")

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about_us")
def about_us():
    return render_template("about_us.html")


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