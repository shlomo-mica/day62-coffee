from wtforms.fields import DateTimeField
from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, Label, SelectField,TimeField
from wtforms.validators import DataRequired, InputRequired, Length, URL
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)
# class wtforms.fields.DateTimeField(default field arguments, format='%Y-%m-%d %H:%M:%S')#
open_time = DateTimeField(format='%Y-%m-%d %H:%M:%S')


class CafeForm(FlaskForm):
    cafe_name = StringField('Coffee type', validators=[DataRequired(message='xxxxx'), Length(min=3, max=7)])
    cafe = Label('Cafe name', text='Cafe name')

    location_url = StringField('Location', validators=[URL(True, message='NOT A URL INPUT')])
    location_label = Label('Cafe Location', text='Cafe Location on Google Maps(url')

    #open_time = StringField('Open Hours', validators=[DataRequired()])
    open_time = TimeField(label="Open H", format='%H:%M')
    close_time = TimeField(label="Close At..", format='%H:%M')

    #close_time = StringField('Close Hours', validators=[DataRequired()])

    coffee_rate_label = Label('Coffee', text='Coffee Rating')
    coffee_rate = SelectField('Coffee_rate',
                              choices=['☕☕☕☕',
                                       '☕☕☕',
                                       '☕☕'])

    wifi_strength_label = Label('Wifi_strength', text='WiFi Strength Rating')
    wifi_strength_rating = SelectField('Wifi_strength', choices=['💪💪',
                                                                 '💪💪💪',
                                                                 '✘'])

    power_socket_labet = Label('power_socket', text='Power Socket Availability')
    power_socket = SelectField('Power_Socket', choices=['🔌🔌🔌', '🔌'])

    close_time_label = Label('close', text='Closing_Time')
    update_your_coffee = SubmitField('Update', validators=[DataRequired()])


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


@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()
    name = request.form.get('cafe_name', 'name')
    location_url = request.form.get('location_url')
    open_time = request.form.get('open_time')
    close_time = request.form.get('close_time')
    coffee_rate = request.form.get('coffee_rate')
    wifi_strength_rating = request.form.get('wifi_strength_rating')
    power_socket = request.form.get('power_socket')
    if form.validate_on_submit():
        print("True")
        print("DATA2-", name, location_url)
        with open('cafe-data.csv', 'a', newline='', encoding='UTF8') as f:
            # create the csv writer
            writer = csv.writer(f)
            writer.writerow(
                [name, location_url, open_time, close_time, coffee_rate, wifi_strength_rating, power_socket])

    # write a row to the csv file

    # spamwriter = csv.writer(csvfile, delimiter=' ',
    #                         quotechar='|', quoting=csv.QUOTE_MINIMAL)
    # spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
    # spamwriter.writerow(['name', 'location_url', 'Wonderful Spam'])
    # create the csv writer
    # write a row to the csv file

    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()

    return render_template('add_coffee.html', form=form)


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

    return render_template('cafes.html', cafes=list_of_rows, test_item=test_item, first_row=first_row)


if __name__ == '__main__':
    app.run(debug=True)
# port 5000
# {% from 'bootstrap5/form.html' import render_form %}
# {{ render_form(form) }}
