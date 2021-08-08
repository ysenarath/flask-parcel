"""
Flask-Parcel
-------------

ParcelJS Extension for Flask
"""

from setuptools import setup

with open("README.md") as fh:
    long_description = fh.read().strip()

with open('requirements.txt') as fh:
    requirements = fh.read().strip().split('\n')

setup(
    name='Flask-Parcel',
    version='0.0.1',
    url='https://github.com/ysenarath/flask-parcel',
    license='MIT',
    author='Yasas Senarath',
    author_email='ysenarath.93@gmail.com',
    description='Run parcel builds alongside flask.',
    long_description=long_description,
    py_modules=['flask_sqlite3'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=requirements,
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
