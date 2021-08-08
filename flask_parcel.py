import os
import shutil
import subprocess
import flask
import jinja2
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
            name, import_name, url_prefix=self.url_prefix,
            static_folder=self.out_dir, static_url_path='/'
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

    def clean(self):
        if os.path.exists(self.out_dir):
            shutil.rmtree(self.out_dir)

    def build(self, inputs, clean=True):
        if clean:
            self.clean()
        if not isinstance(inputs, list):
            inputs = [inputs]
        input_files = (os.path.join(self.template_folder, _input) for _input in inputs)
        args = ('parcel', 'build', *input_files, '-d', self.out_dir, '--public-url', self.url_prefix, '--no-minify')
        _parcel = subprocess.run(args)

    def render_template(self, name, *args, **kwargs):
        template = self._jinja_env.get_template(name)
        return template.render(*args, **kwargs)

    @property
    def _jinja_env(self):
        if not hasattr(self, '_prop_jinja_env'):
            self._prop_jinja_env = jinja2.Environment(
                loader=jinja2.FileSystemLoader(self.out_dir),
                autoescape=jinja2.select_autoescape()
            )
        return self._prop_jinja_env
