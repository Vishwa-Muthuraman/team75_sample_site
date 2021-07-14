from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, DecimalField, FloatField, DateField
from wtforms.validators import DataRequired, NumberRange, Email, Length
from datetime import date

class VolunteerForm(FlaskForm):
    # create attributes
    student_name = StringField("Please enter your full name", validators=[DataRequired()])
    student_ID = StringField("Please enter your student ID", validators=[DataRequired()])
    hours = DecimalField("Please enter the number of hours worked: ",validators=[DataRequired(), NumberRange(max=10)])

    event = SelectField("Select which event you attended",
                 choices=[('Food Drive (7/13/2021)', 'Food Drive (7/13/2021)'),('Quaransteam (7/19/2021)', 'Quaransteam (7/19/2021)'),('IBM (7/19-23/2021)', 'IBM (7/19-23/2021)'),('WISE Prep Work(LEADS ONLY)', 'WISE Prep Work(LEADS ONLY)'), ('WISTEM2D Prep Work(LEADS ONLY)', 'WISTEM2D Prep Work(LEADS ONLY)'),('Food Drive Prep Work(LEADS ONLY)', 'Food Drive Prep Work(LEADS ONLY)'), ('Charity Miles Prep Work(LEADS ONLY)', 'Charity Miles Prep Work(LEADS ONLY)'),('Stem Kits Prep Work(LEADS ONLY)', 'Stem Kits Prep Work(LEADS ONLY)'),('Raider Pollinators Prep Work(LEADS ONLY)','Raider Pollinators Prep Work(LEADS ONLY)'),('Safety Prep Work(LEADS ONLY)','Safety Prep Work(LEADS ONLY)'),('Animal Shelter Prep Work(LEADS ONLY)','Animal Sheler Prep Work(LEADS ONLY)'),('FLL BoroBlast Prep Work(LEADS ONLY)', 'FLL BoroBlast Prep Work(LEADS ONLY)'), ('IBM Prep Work(LEADS ONLY)', 'IBM Prep Work(LEADS ONLY)'),('Quaransteam Prep Work(LEADS ONLY)','Quaransteam Prep Work(LEADS ONLY)'),('Precious Plastics Prep Work(LEADS ONLY)', 'Precious Plastics Prep Work(LEADS ONLY)'),('Team Website Prep Work(LEADS ONLY)','Team Website Prep Work(LEADS ONLY)'), ('Outreach Tracking Website Prep Work(LEADS ONLY)','Outreach Tracking Website Prep Work(LEADS ONLY)')])
   
    #Date = StringField("Enter the date your filling out this form in the format month-date-year(6-22-2021)", validators=[DataRequired(), Length(max =10)])
    Date = DateField("Enter the date", default=date.today)
    
    submit = SubmitField("Enter")


class SpecificUser(FlaskForm):
    # create attributes
    student_ID = StringField("Please enter your Student ID", validators=[DataRequired()])
 
    submit = SubmitField("Enter")



