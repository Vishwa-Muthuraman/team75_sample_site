from flask import render_template, redirect, url_for, flash
from app import app, db
import forms
from models import Volunteers
from datetime import datetime


@app.route('/')
@app.route('/index', methods=['GET','POST'])
def index():

    form = forms.VolunteerInfo()

    if form.validate_on_submit():
        print('Validated')
        # return render_template('recent_volunteers.html', form=form)
        student_name = form.student_name.data
        event = form.event.data
        hours = form.hours.data

        v = Volunteers(name=student_name, event=event, hours=hours)

        db.session.add(v)
        db.session.commit()
        flash('Data submitted')
        
        return redirect(url_for('recent_volunteers'))

    return render_template('index.html', form=form)

@app.route('/recent_volunteers')
def recent_volunteers():

    volunteers = Volunteers.query.all()

    return render_template('recent_volunteers.html', volunteers=volunteers)

@app.route('/home')
def home():
    return render_template('home.html')
