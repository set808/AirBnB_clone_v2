#!/usr/bin/python3
''' Starts a Flask app'''
from models import storage
from flask import Flask, render_template


app = Flask(__name__)
app.url_map.strict_slashes = False
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

@app.route('/states_list')
def states_list():
    return render_template('7-states_list.html', storage=storage.all('State'))

@app.teardown_appcontext
def close(exception):
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
