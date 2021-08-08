import flask
from flask import Flask

from flask_parcel import Parcel

parcel = Parcel()

parcel.build(inputs=[
    'partials/header.html',
    'index.html',
])

# app

app = Flask(__name__)

parcel.init_app(app)


@app.route('/get_name')
def get_name():
    return flask.jsonify({
        'name': 'Admin'
    })


@app.route('/')
def index():
    return parcel.render_template('index.html', message='This is a message from Jinja')
