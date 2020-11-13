# Flask Session object grabs user data and can pass to template
from flask import Flask, render_template, session, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import (StringField, BooleanField, DateTimeField, RadioField,
                     SelectField, TextField, TextAreaField, SubmitField)
# Flask validators allow you to check what data is being submitted
from wtforms.validators import DataRequired


app = Flask(__name__)

# configure app with key - still local for now, so will reconfigure later
app.config['SECRET_KEY'] = 'mykey'

# later, put in own .py file to be cleaner
class InfoForm(FlaskForm):
    # create attributes
    breed = StringField('What breed is the dog?', validators=[DataRequired()])
    neutered = BooleanField('Has the dog been neutered?')
    mood = RadioField('Please choose your mood:',
                      choices=[('mood_one', 'Happy'), ('mood_two', 'Excited')])
    food_choice = SelectField(u'Pick their favorite food: ',
                              choices=[('chi','Chicken'), ('bf','Beef'),('fish','Fish')])
    feedback = TextAreaField()
    submit = SubmitField('Submit')


@app.route('/', methods=['GET','POST'])
def index():
    form = InfoForm()

    if form.validate_on_submit():
        # update session object
        session['breed'] = form.breed.data
        session['neutered'] = form.neutered.data
        session['mood'] = form.mood.data
        session['food'] = form.food_choice.data
        session['feedback'] = form.feedback.data

        # automatically have a form redirect on submission, keeps template files
        # simple as possible. Only get thank you page on valid submission
        return redirect(url_for('thankyou'))

    return render_template('index.html', form=form)

@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')

if __name__ == '__main__':
    app.run(debug=True)
