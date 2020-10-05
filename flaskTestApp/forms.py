from flaskTestApp import app
from flask_wtf import FlaskForm #Comment on how to install via terminal: pip install Flask-WTF
from wtforms import StringField, IntegerField, DateField, RadioField, SelectField

class SampleForm(FlaskForm):
    first_name = StringField("First Name")
    last_name = StringField("Last Name")
    panther_id = IntegerField("Panther ID")
    start_date = DateField("Start Date", format='%m/%d/%Y')
    major = RadioField("Major",
                       choices=[('it','Information Technology'),
                                ('cs','Computer Science')])
    campus = SelectField("Campus",
                         choices=[('mmc',"MMC"),
                                  ('bbc','BBC'),
                                  ('ec',"Engineering Center")])