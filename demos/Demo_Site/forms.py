from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, DecimalField
from wtforms.validators import DataRequired, NumberRange, Email

class NewUser(FlaskForm):
    student_name = StringField("Please enter your name", validators=[DataRequired()])

class VolunteerInfo(FlaskForm):

    student_name = StringField("Please enter your full name", validators=[DataRequired()])
    event = SelectField("Event: ",
                        choices=[('WISE', 'WISE'),('WiSTEM2D','WiSTEM2D'), ('FIRST', 'FIRST')])


    hours = DecimalField("Please enter the number of hours worked: ",validators=[DataRequired(), NumberRange(max=10)])
    submit = SubmitField("Enter")
