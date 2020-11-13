from app import app
from flask import render_template

import forms

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/add', methods=['GET','POST'])
def add():
    form = forms.addTaskForm()

    if form.validate_on_submit():
        # prints out to terminal
        print(f"Submitted task: {form.title.data}")
        # add SQL connectivity here
        return render_template('add.html', form=form, title=form.title.data)

    return render_template('add.html', form=form)
