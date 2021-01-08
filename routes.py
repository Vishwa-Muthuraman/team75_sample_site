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
        form = forms.VolunteerForm()
        eventregist = EventRegist.query.filter_by(stud_ID=form.student_ID.data)
        return render_template('volunteer_found.html', eventregist=eventregist)

    return render_template('sign_up.html', form=form)

@app.route('/specific_volunteers', methods=['GET', 'POST'])
def indx():
    form = forms.SpecificUser()

    if form.validate_on_submit():
        # update session object
        print('Validated')  
     
        return redirect(url_for('volunteer_found'))

    return render_template('specific_volunteers.html', forms=form)

@app.route('/volunteer_found', methods=['GET', 'POST'])
def volunteer_found():
        form = forms.SpecificUser()
        if (form.student_ID.data=='84362345'):
            stud_eventregist = EventRegist.query.all()
        else :
            stud_eventregist = EventRegist.query.filter_by(stud_ID=form.student_ID.data)
        return render_template('volunteer_found.html', studregist=stud_eventregist)

# @app.route('/volunteer_found', methods=['GET', 'POST'])
# def volunteer_fnd():
            