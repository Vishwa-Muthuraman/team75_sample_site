from tkinter.constants import DISABLED
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
                 choices=[('WISE', 'WISE'),('WISE Prep Work(LEADS ONLY)', 'WISE Prep Work(LEADS ONLY)') ,('WISTEM2D', 'WISTEM2D'), ('WISTEM2D Prep Work(LEADS ONLY)', 'WISTEM2D Prep Work(LEADS ONLY)'),('Food Drive', 'Food Drive'),('Food Drive Prep Work(LEADS ONLY)', 'Food Drive Prep Work(LEADS ONLY)'),('Charity Miles','Charity Miles'), ('Charity Miles Prep Work(LEADS ONLY)', 'Charity Miles Prep Work(LEADS ONLY)'),('Stem Kits', 'Stem Kits'),('Stem Kits Prep Work(LEADS ONLY)', 'Stem Kits Prep Work(LEADS ONLY)'),('Raider Pollinators', 'Raider Pollinators'),('Raider Pollinators Prep Work(LEADS ONLY)','Raider Pollinators Prep Work(LEADS ONLY)'), ('Safety', 'Safety'),('Safety Prep Work(LEADS ONLY)','Safety Prep Work(LEADS ONLY)'),('Animal Shelter','Animal Shelter'),('Animal Shelter Prep Work(LEADS ONLY)','Animal Sheler Prep Work(LEADS ONLY)'), ('FLL BoroBlast', 'FLL BoroBlast'),('FLL BoroBlast Prep Work(LEADS ONLY)', 'FLL BoroBlast Prep Work(LEADS ONLY)'), ('IBM', 'IBM'), ('IBM Prep Work(LEADS ONLY)', 'IBM Prep Work(LEADS ONLY)'), ('Quaransteam', 'Quaransteam'),('Quaransteam Prep Work(LEADS ONLY)','Quaransteam Prep Work(LEADS ONLY)'),('Precious Plastics', 'Precious Plastics'),('Precious Plastics Prep Work(LEADS ONLY)', 'Precious Plastics Prep Work(LEADS ONLY)'),('Outreach Tracking Website Prep Work(LEADS ONLY)','Outreach Tracking Website Prep Work(LEADS ONLY)'),('Team Website Prep Work(LEADS ONLY)','Team Website Prep Work(LEADS ONLY)')])
   
    #Date = SelectField("Type the date you are entering the form",
     #           choices= [('January', 'January'),('February', 'February'), ('March', 'March'), ('April', 'April'), ('May', 'May'), ('June', 'June'), ('July', 'July'), ('August', 'August'),('September', 'September'), ('October', 'October'), ('November', 'November'), ('December', 'December')])
      #Date_day = SelectField("Type the date you are entering the form",
       #         choices = [('1'), ('2','2'), ('3','3'), ('4','4'), ('5','5'), ('6','6'), ('7','7'), ('8','8'), ('9','9'), ('10','10'), ('11','11'), ('12','12'), ('13','13'), ('14','14'), ('15','15'), ('16','16'), ('17','17'), ('18','18'), ('19','19'), ('20','20'), ('21','21'), ('22','22'), ('23','23'), ('24','24'), ('25','25'), ('26','26'), ('27','27'), ('28','28'), ('29','29'), ('30','30'), ('31','31')])
       #         choices = [('2020',)]
    
#year = DecimalField("Enter a year", validators=[DataRequired()])
#month = DecimalField("Enter a month", validators=[DataRequired()])
#day = DecimalField("Enter a day", validators=[DataRequired()])
   
#Date = datetime.date(year, month, day)
#Date = datetime.date(year, month, day)
#Date = DateTimeField("Enter the date you are filling out this form in the format (Month-Day-Year)Ex: 6-15-2021",validators=[DataRequired()], format='%Y-%m-%d')
    #Date = StringField("Enter the date your filling out this form in the format month-date-year(6-22-2021)", validators=[DataRequired(), Length(max =10)])
    Date = DateField("Enter the date", default=date.today)
    
    submit = SubmitField("Enter")


class SpecificUser(FlaskForm):
    # create attributes
    student_ID = StringField("Please enter your Student ID", validators=[DataRequired()])
 
    submit = SubmitField("Enter")



