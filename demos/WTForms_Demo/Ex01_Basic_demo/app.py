from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

# instantiate Flask App
app = Flask(__name__)

# create security key - much more secure ways to deploy this later
# e.g. someone might be able to get access to this .py file and see
# the password (an environment variable would be more secure)
app.config['SECRET_KEY'] = 'mysecretkey12345'

# create instance of form class we want, inherit from FlaskForm
class InfoForm(FlaskForm):
    """Docstring: """
    # attributes of the class InfoForm
    breed = StringField("What breed are you?")
    submit = SubmitField("Submit")

# set up view
@app.route('/', methods=['GET','POST'])
@app.route('/index')
def index():
    # preallocate for looping
    breed = False

    # create instance of the InfoForm
    form = InfoForm()

    # check that all validators were correct (i.e. data present)
    if form.validate_on_submit():
        # grab breed data submitted
        breed = form.breed.data
        # reset
        form.breed.data = ''

    return render_template('index.html', form=form, breed=breed)

if __name__ =='__main__':
    app.run(debug=True)
