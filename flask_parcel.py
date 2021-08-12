import os
import shutil
import subprocess
import jinja2
from flask import Blueprint

__all__ = [
    'Parcel',
]

PARCEL_TEMPLATE = '''
<div style="position: absolute; bottom: 10px; right: 10px;">
    <button style="background-color: transparent; border: none; padding: 0; margin: 0;"
            onclick="fetch('{url_prefix}/build')
            .then(response => response.json())
            .then(data => window.location.reload());">⟳
    </button>
</div>
'''


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
        self._input_files = []
        self.app = app
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        if app.debug:
            self.blueprint.route('/build')(self.build)
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

    def add_input(self, inputs):
        if not isinstance(inputs, list):
            inputs = [inputs]
        self._input_files += [os.path.join(self.template_folder, _input) for _input in inputs]

    def build(self, clean=True):
        if os.path.exists(self.out_dir) and (not clean):
            return
        if os.path.exists(self.out_dir):
            self.clean()
        minify = True
        args = ('parcel', 'build', *self._input_files, '-d', self.out_dir, '--public-url', self.url_prefix,
                *(['--no-minify'] if not minify else []))
        _parcel = subprocess.run(args)
        return {
            'status': 'success',
            'data': {}
        }

    def render_template(self, name, *args, **kwargs):
        template = self._jinja_env.get_template(name)
        if self.app.debug:
            parcel_template = PARCEL_TEMPLATE.format(url_prefix=self.url_prefix)
            return template.render(*args, **kwargs) + parcel_template
        else:
            return template.render(*args, **kwargs)

    @property
    def _jinja_env(self):
        if not hasattr(self, '_prop_jinja_env'):
            self._prop_jinja_env = jinja2.Environment(
                loader=jinja2.FileSystemLoader(self.out_dir),
                autoescape=jinja2.select_autoescape(),

            )
            self._prop_jinja_env.globals['parcel'] = self
        return self._prop_jinja_env
