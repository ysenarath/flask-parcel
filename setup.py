"""
Flask-Parcel
-------------

ParcelJS Extension for Flask
"""
import setuptools

with open("README.md") as fh:
    long_description = fh.read().strip()

setuptools.setup(
    name='Flask-Parcel',
    version='0.0.2',
    url='https://github.com/ysenarath/flask-parcel',
    license='MIT',
    author='Yasas Senarath',
    author_email='ysenarath.93@gmail.com',
    description='Run parcel builds alongside flask.',
    long_description=long_description,
    py_modules=['flask_parcel'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=['Flask'],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        "License :: OSI Approved :: MIT License",
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
