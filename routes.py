from flask import render_template, redirect, url_for, flash
from app import app, db
import forms
from models import EventRegist
from datetime import datetime

@app.route('/')

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

@app.route('/sign_up', methods=['GET','POST'])
def index():
    form = forms.VolunteerForm()

    if form.validate_on_submit():
        # update session object
        print('Validated')
        student_name = form.student_name.data
        student_ID = form.student_ID.data
        hours = form.hours.data
        event = form.event.data

        v = EventRegist(name=student_name, stud_ID=student_ID, hours=hours, event=event)

        db.session.add(v)
        db.session.commit()
        flash('Data Submitted')
                
        return redirect(url_for('recent_volunteers'))

    return render_template('sign_up.html', form=form)

@app.route('/recent_volunteers')
def recent_volunteers():
    eventregist = EventRegist.query.all()
    return render_template('recent_volunteers.html', eventregist=eventregist)