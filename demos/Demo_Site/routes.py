from flask import render_template, redirect, url_for, flash, Response
from app import app, db
import forms
from models import Volunteers
from datetime import datetime

import io
import os
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import seaborn as sns
sns.set()

@app.route('/')
@app.route('/index', methods=['GET','POST'])
def index():

    form = forms.VolunteerInfo()

    if form.validate_on_submit(): # if true, then form was successfully submitted
        #print('Validated')
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

    # grab data
    volunteers = Volunteers.query.filter_by(name='Matt')

    total_hours = 0
    event, hours = [], []

    for data in volunteers:
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
    if os.path.exists("static/images/plot.png"):
        os.remove("static/images/plot.png")

    fig = plt.figure()
    axis = fig.add_subplot(1,1,1)

    # documentation
    # https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.axes.Axes.bar.html
    axis.bar(gb.Event, gb.Hours, color='blue')
    axis.set_title("Matt's Total Hours Volunteered", fontsize=16)
    axis.set_ylabel("Hours", fontsize=14)
    axis.set_xlabel("Event", fontsize=14)

    plt.savefig('static/images/plot.png')

    return render_template('recent_volunteers.html', volunteers=volunteers,
                           url='static/images/plot.png')


@app.route('/plot.png')
def plot_png():
    # grab data
    volunteers = Volunteers.query.filter_by(name='Matt')

    total_hours = 0
    event, hours = [], []

    for data in volunteers:
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
    if os.path.exists("static/images/plot.png"):
        os.remove("static/images/plot.png")

    fig = plt.figure()
    axis = fig.add_subplot(1,1,1)

    # documentation
    # https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.axes.Axes.bar.html
    axis.bar(gb.Event, gb.Hours, color='blue')
    axis.set_title("Matt's Total Hours Volunteered", fontsize=16)
    axis.set_ylabel("Hours", fontsize=14)
    axis.set_xlabel("Event", fontsize=14)


    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)

    return Response(output.getvalue(), mimetype='image/png')


@app.route('/home')
def home():
    return render_template('home.html')
  