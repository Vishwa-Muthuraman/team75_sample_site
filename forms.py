from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, DecimalField, FloatField, DateField
from wtforms.validators import DataRequired, NumberRange, Email, Length
from datetime import date

class VolunteerForm(FlaskForm):
    # create attributes
    student_name = StringField("Please enter your full name", validators=[DataRequired()])
    student_ID = StringField("Please enter your student ID", validators=[DataRequired()])
    hours = DecimalField("Please enter the number of hours worked(maximum hours per submission = 10)(Ex: 1 hour & 30 minutes = 1.5): ",validators=[DataRequired(), NumberRange(max=10)])

    event = SelectField("Select which event you attended",
                 choices=[

                            ('Charity Miles (School year)','Charity Miles (School year)'),
                            ('Homework Help (School Year)','Homework Help (School Year)'),
                            ('RoboSmiles - Cards for healthcare workers(2/17-21/2022)','RoboSmiles - Cards for healthcare workers(2/17-21/2022)'),

                            ('Executive Member Hours','Executive Member Hours'),
                            ('GSRM Prep Work', 'GSRM Prep Work'),
                            ('RoboSmiles Prep Work (Leads Only)','RoboSmiles Prep Work (Leads Only)'),
                            ('Homework Help Prep Work (LEADS ONLY)','Homework Help Prep Work (LEADS ONLY)'),
                            ('RoboCreators Initiative Prep Work','RoboCreators Initiative Prep Work'),
                            ('WISE Prep Work(LEADS ONLY)', 'WISE Prep Work(LEADS ONLY)'),
                            ('WISTEM2D Prep Work(LEADS ONLY)', 'WISTEM2D Prep Work(LEADS ONLY)'),
                            ('Food Drive Prep Work(LEADS ONLY)', 'Food Drive Prep Work(LEADS ONLY)'),
                            ('Charity Miles Prep Work(LEADS ONLY)', 'Charity Miles Prep Work(LEADS ONLY)'),
                            ('Stem Kits Prep Work(LEADS ONLY)', 'Stem Kits Prep Work(LEADS ONLY)'),
                            ('Raider Pollinators Prep Work(LEADS ONLY)','Raider Pollinators Prep Work(LEADS ONLY)'),
                            ('Safety Prep Work(LEADS ONLY)','Safety Prep Work(LEADS ONLY)'),
                            ('Animal Shelter Prep Work(LEADS ONLY)','Animal Sheler Prep Work(LEADS ONLY)'),
                            ('FLL BoroBlast Prep Work(LEADS ONLY)', 'FLL BoroBlast Prep Work(LEADS ONLY)'),
                            ('IBM Prep Work(LEADS ONLY)', 'IBM Prep Work(LEADS ONLY)'),
                            ('Quaransteam Prep Work(LEADS ONLY)','Quaransteam Prep Work(LEADS ONLY)'),
                            ('Precious Plastics Prep Work(LEADS ONLY)', 'Precious Plastics Prep Work(LEADS ONLY)'),
                            ('Team Website Prep Work(LEADS ONLY)','Team Website Prep Work(LEADS ONLY)'),
                            ('Outreach Tracking Website Prep Work(LEADS ONLY)','Outreach Tracking Website Prep Work(LEADS ONLY)')])
   
    Date = DateField("Enter the date", default=date.today)
    
    submit = SubmitField("Enter")


class SpecificUser(FlaskForm):
    # create attributes
    student_ID = StringField("Please enter your Student ID", validators=[DataRequired()])
 
    submit = SubmitField("Enter")
