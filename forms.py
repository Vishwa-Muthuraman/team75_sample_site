from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, DecimalField
from wtforms.validators import DataRequired, NumberRange, Email

class NewUser(FlaskForm):
    student_name = StringField("Please enter your name", validators=[DataRequired()])
    student_ID = StringField("Please enter your student ID", validators=[DataRequired()])

class VolunteerForm(FlaskForm):
    # create attributes
    student_name = StringField("Please enter your full name", validators=[DataRequired()])
    student_ID = StringField("Please enter your student ID", validators=[DataRequired()])
    hours = DecimalField("Please enter the number of hours worked: ",validators=[DataRequired(), NumberRange(max=10)])

    event = SelectField("Select which event you attended",
                 choices=[('WISE', 'WISE'), ('Food Drive', 'Food Drive')])

    submit = SubmitField("Enter")

class SpecificUser(FlaskForm):
    # create attributes
    stud_ID = StringField("Please enter your student ID", validators=[DataRequired()])

    submit = SubmitField("Enter")



