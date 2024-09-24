from flask_bootstrap import Bootstrap
from flask import Flask,render_template, session,redirect,url_for,flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,validators
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config["SECRET_KEY"] = "babababa"

def uoft_email_validator(form,field):
    if 'utoronto' not in field.data or not field.data.endswith('@mail.utoronto.ca'):
        raise validators.ValidationError('Email must be a valid UofT Email')

class NameForm(FlaskForm):
    name = StringField("What is your name?", validators=[DataRequired()])
    email = StringField("What is your email?",validators=[DataRequired(),uoft_email_validator])
    submit = SubmitField("Submit")

@app.route("/",methods=['GET','POST'])
def index():
    name = "Stranger"
    email = None
    form = NameForm()
    
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('Looks like you have changed your name!')
        name = session['name'] = form.name.data  
    if form.validate_on_submit():
        old_email = session.get('email')
        if old_email is not None and old_email != form.email.data:
            flash('Looks like you have changed your email!')
        email = session['email'] = form.email.data  
    return render_template('index.html',form=form,name=name,email=email)



bootstrap = Bootstrap(app)
