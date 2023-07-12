import wtforms.validators
from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, Label, SelectField
from wtforms.validators import DataRequired, InputRequired, Length
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


class CafeForm(FlaskForm):
    cafe_name = StringField('coffee type', validators=[DataRequired(message='xxxxx'), Length(min=3, max=7)])
    cafe = Label('Cafe name', text='Cafe name')

    location_url = StringField('Location', validators=[InputRequired()])
    location_label = Label('Cafe Location', text='Cafe Location on Google Maps(url')

    open_time = StringField('Open', validators=[DataRequired()])
    open_time_label = Label('open', text='Opening Time')

    close_time_label = Label('close', text='Closing_Time')
    close = SubmitField('Close', validators=[DataRequired()])

    coffee_rate_label = Label('Coffee', text='Coffee Rating')
    coffee_rate = SelectField('Coffee_rate',
                              choices=[('tr', 'trina'),
                                       ('lo', 'longi'),
                                       ('ph', 'phono'),
                                       ('leap', 'leapton')])
    wifi_strength_label = Label('wifi_strangth', text='WiFi Strength Rating')
    wifi_strength_rating = SelectField('Wifi_strength', choices=[('tr', 'trina'),
                                                                 ('lo', 'longi'),
                                                                 ('ph', 'phono'),
                                                                 ('leap', 'leapton')])

    power_socket_labet = Label('power_socket', text='Power Socket Availability')
    power_socket_availability = SelectField('Power_Sockrt', choices=[('tr', 'trina'),
                                                                     ('lo', 'longi'),
                                                                     ('ph', 'phono'),
                                                                     ('leap', 'leapton')])


# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
# e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add')
def add_cafe():
    form = CafeForm()

    if form.validate_on_submit():
        print("True")
    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    col_name = CafeForm()
    test_item = 'TEST'
    first_row = ['Lighthaus', 'https://goo.gl/maps/2EvhB4oq4gyUXKXx9', '11AM', ' 3:30PM', '☕☕☕☕️', '💪💪', '🔌🔌🔌']
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    print((list_of_rows))
    return render_template('cafes.html', cafes=list_of_rows, test_item=test_item, first_row=first_row)


if __name__ == '__main__':
    app.run(debug=True)
# port 5000
# {% from 'bootstrap5/form.html' import render_form %}
# {{ render_form(form) }}
