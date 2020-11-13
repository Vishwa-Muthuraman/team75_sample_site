from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class addTaskForm(FlaskForm):
    title = StringField('Task title', validators=[DataRequired()])
    submit = SubmitField('Submit')
