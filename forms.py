from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, DecimalField 
from wtforms.validators import DataRequired, NumberRange, Email
import datetime

class VolunteerForm(FlaskForm):
    # create attributes
    student_name = StringField("Please enter your full name", validators=[DataRequired()])
    student_ID = StringField("Please enter your student ID", validators=[DataRequired()])
    hours = DecimalField("Please enter the number of hours worked: ",validators=[DataRequired(), NumberRange(max=10)])

    event = SelectField("Select which event you attended",
                 choices=[('WISE', 'WISE'), ('Food Drive', 'Food Drive'),('ARIS STEM Summit','ARIS STEM Summit'), ('Charity Miles','Charity Miles')])

    submit = SubmitField("Enter")


class SpecificUser(FlaskForm):
    # create attributes
    student_ID = StringField("Please enter your Student ID", validators=[DataRequired()])
 
    submit = SubmitField("Enter")

class GeneralAccount(FlaskForm):
    student_name = StringField("Please enter your full name", validators=[DataRequired()])
    student_ID = StringField("Please enter your student ID", validators=[DataRequired()])
    grad_year = StringField("Please enter your graduation year", validators=[DataRequired()])
    student_email = StringField("Please enter your school email",validators=[DataRequired()])
    subteam = SelectField("Select your subteam",
                        choices=[('Executive Leadership', 'Executive Leadership'),
                                ('Documentation', 'Documentation'), ('Public Relations', 'Public Relations'),
                                ('Finance','Finance'),('Strategy','Strategy'),
                                ('Design','Design'), ('Mechanical','Mechanical'),
                                ('Electrical','Electrical'),('Supplementary','Supplementary'),
                                ('Programming','Programming'),('Safety','Safety')])
    submit = SubmitField("Enter")



