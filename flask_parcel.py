import os
import subprocess
import flask
from flask import Blueprint

__all__ = [
    'Parcel',
]


class Parcel:
    def __init__(self, app=None, name='Parcel', import_name='parcel', url_prefix='/parcel',
                 template_folder='./templates', out_dir='./build/output'):
        self.name = name
        self.template_folder = template_folder
        self.out_dir = out_dir
        self.url_prefix = url_prefix
        self.blueprint = Blueprint(
            name, import_name, url_prefix=self.url_prefix, static_folder=self.out_dir,
            static_url_path='/', template_folder=self.template_folder
        )
        self.app = app
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        app.register_blueprint(self.blueprint)
        self.app = app

    @property
    def template_folder(self):
        return self._template_folder

    @template_folder.setter
    def template_folder(self, value):
        self._template_folder = os.path.abspath(value)

    @property
    def out_dir(self):
        return self._out_dir

    @out_dir.setter
    def out_dir(self, value):
        self._out_dir = os.path.abspath(value)

    def build(self, *inputs):
        input_files = (os.path.join(self.template_folder, _input) for _input in inputs)
        args = ('parcel', 'build', *input_files, '-d', self.out_dir, '--public-url', self.url_prefix)
        _parcel = subprocess.run(args)

    def render_template(self, path, *args, **kwargs):
        input_path = os.path.join(self.out_dir, path)
        if os.path.exists(input_path):
            with open(input_path, 'r', encoding='utf-8') as fp:
                return flask.render_template_string(fp.read(), **kwargs)
        return flask.render_template(*args, **kwargs)
