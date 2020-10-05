from flaskTestApp import app, forms
from flask import request, render_template


@app.route('/')
def helloWeb():
    first_name = "Nestor"
    last_name = "Hernandez"
    return "I am {0} {1}.".format(first_name,last_name)

@app.route('/page1')
def page1():
    return "page1"

@app.route('/search',methods=['GET','POST'])
def search():
    my_sample_form = forms.SampleForm(request.form)

    if request.method == "POST":
        first_name = request.form["first_name"]
        last_name = request.form['last_name']
        panther_id = request.form['panther_id']
        start_date = request.form['start_date']
        major = request.form['major']
        campus = request.form['campus']

        response = [first_name, last_name, panther_id, start_date, major, campus]

        return render_template('results.html',response=response, form=my_sample_form, major = major)

    return render_template('search.html', form=my_sample_form)