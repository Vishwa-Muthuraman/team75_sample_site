from flask import render_template, redirect, url_for, flash, Response
from app import app, db
import forms
from models import DATABASE_URL
from models import StudentRegist
from datetime import datetime

import io
import os
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import seaborn as sns
sns.set()
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

        v = DATABASE_URL(name=student_name, stud_ID=student_ID, hours=hours, event=event)

        db.session.add(v)
        db.session.commit()
        flash('Data Submitted')
        form = forms.VolunteerForm()
        database_url = DATABASE_URL.query.filter_by(stud_ID=form.student_ID.data)
        return render_template('volunteer_found.html', DATABASE_URL=database_url)

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
            stud_eventregist = DATABASE_URL.query.all()
        else :
            stud_eventregist = DATABASE_URL.query.filter_by(stud_ID=form.student_ID.data)

        total_hours = 0
        event, hours = [], []

        for data in stud_eventregist:
            # add up all hours volunteered
            total_hours += data.hours

            # save to list elements
            event.append(data.event)
            hours.append(data.hours)

        # convert to pandas dataframe
        df = pd.DataFrame({"Event": event, "Hours": hours})
        print(df)
        #
        gb = df.groupby('Event').sum().reset_index()
        print(gb)

        # remove image if it exits
        if os.path.exists("plot.png"):
            os.remove("plot.png")

        fig = plt.figure()
        axis = fig.add_subplot(1,1,1)

        # documentation
        # https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.axes.Axes.bar.html
        axis.bar(gb.Event, gb.Hours, color='blue')
        axis.set_title("Total Hours Volunteered", fontsize=16)
        axis.set_ylabel("Hours", fontsize=14)
        axis.set_xlabel("Event", fontsize=14)

        plt.savefig('plot.png')

        return render_template('volunteer_found.html', studregist=stud_eventregist, url='plot.png')

# @app.route('/volunteer_found', methods=['GET', 'POST'])
# def volunteer_fnd():
@app.route('/plot.png')
def plot_png():
    # grab data
    form = forms.SpecificUser()
    eventregist = DATABASE_URL.query.filter_by(stud_ID=form.student_ID.data)

    total_hours = 0
    event, hours = [], []

    for data in eventregist:
        # add up all hours volunteered
        total_hours += data.hours

        # save to list elements
        event.append(data.event)
        hours.append(data.hours)

    # convert to pandas dataframe
    df = pd.DataFrame({"Event": event, "Hours": hours})

    #
    gb = df.groupby('Event').sum().reset_index()
    print(gb)

    # remove image if it exits
    if os.path.exists("plot.png"):
        os.remove("plot.png")

    fig = plt.figure()
    axis = fig.add_subplot(1,1,1)

    # documentation
    # https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.axes.Axes.bar.html
    axis.bar(gb.Event, gb.Hours, color='blue')
    axis.set_title("Total Hours Volunteered", fontsize=16)
    axis.set_ylabel("Hours", fontsize=14)
    axis.set_xlabel("Event", fontsize=14)


    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)

    return Response(output.getvalue(), mimetype='image/png')