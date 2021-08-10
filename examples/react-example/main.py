import flask
from flask_parcel import Parcel
from flask import Flask

app = Flask(__name__)

# ----------------------------------------------------------------------------------------------------------------------

parcel = Parcel()

parcel.add_input(inputs=['partials/header.html', 'index.html'])

parcel.build()

# ----------------------------------------------------------------------------------------------------------------------

parcel.init_app(app)


@app.route('/get_name')
def get_name():
    return flask.jsonify({
        'name': 'Admin'
    })


@app.route('/')
def index():
    return parcel.render_template('index.html', message='This is a message from Jinja')
