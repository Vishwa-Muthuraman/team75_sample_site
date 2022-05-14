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
                            ('STEM through Gaming','STEM through Gaming'),
                            ('HES STEM Fair (5/20/22)','HES STEM Fair (5/20/22)'),
                            ('Hour of Code Initiative (Prep Hours)','Hour of Code Initiative (Prep Hours)'),
                            ('RoboSmiles Teacher\'s Appreciation Cards (5/1-7/2022)','RoboSmiles Teacher\'s Appreciation Cards (5/1-7/2022)'),
                            ('Field Day Help (4/30/2022)','Field Day Help (4/30/2022)'),
                            ('ShopRite Bagging Initiative(4/16/2022)','ShopRite Bagging Initiative(4/16/2022)'),
                            ('Crocheting Initiative','Crocheting Initiative'),
                            ('St. Jude Donation Drive', 'St. Jude Donation Drive'),
                            ('STEM Summit (3/26/2022)', 'STEM Summit (3/26/2022)'),
                            ('RoboSmiles Easter Event (3/19/2022-4/5/2022)','RoboSmiles Easter Event (3/19/2022-4/5/2022)'),
                            ('Charity Miles (School year)','Charity Miles (School year)'),
                            ('Homework Help (School Year)','Homework Help (School Year)'),

                            ('Executive Member Hours','Executive Member Hours'),
                            ('Crocheting Prep Hours (Leads Only)','Crocheting Prep Hours (Leads Only)'),
                            ('STEM Summit Prep Work (Leads Only)','STEM Summit Prep Work (Leads Only)'),
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
