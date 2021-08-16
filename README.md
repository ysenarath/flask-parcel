# flask-parcel

Parcel Extension for Flask. Automates the build process of your node assets and serve them as static files. 
Additionally, you can use the build assets as Jinja2 templates and inject your values when serving. 

# Installing

1. Install [NodeJS](https://nodejs.org/)
2. Install Flask (https://pypi.org/project/Flask/)
3. Install Flask-Parcel using `pip install Flask-Parcel`

# A Simple Example

```python
from flask import Flask
from flask_parcel import Parcel

parcel = Parcel()

parcel.add_input(inputs=['index.html'])

parcel.build()

app = Flask(__name__)

parcel.init_app(app)

@app.route("/")
def hello():
    return parcel.render_template('index.html')
```

```shell
$ flask run
  * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```