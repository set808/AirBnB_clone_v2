#!/usr/bin/python3
'''Defines a Flask App'''
from flask import Flask


app = Flask('__name__')
app.url_map.strict_slashes = False

@app.route('/')
def hello():
    return "Hello HBNB!"

@app.route('/hbnb')
def hbnb():
    return 'HBNB'

@app.route('/c/<text>')
def c(text):
    return 'C {:s}'.format(text.replace('_', ' '))

@app.route('/python', defaults={'text': 'is cool'})
@app.route('/python/<text>')
def python_text(text):
    return 'Python {:s}'.format(text.replace('_', ' '))

if __name__ == '__main__':
    app.run(host='0.0.0.0')
