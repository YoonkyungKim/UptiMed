import json

from flask import Flask, render_template, redirect, url_for, request, make_response
from options import DEFAULTS

# always refer to yourself
app = Flask(__name__)

def get_saved_data():
    try:
        data = json.loads(request.cookies.get('character'))
    except TypeError:
            data = {}
    return data

@app.route('/')
def index():
    return render_template("index.html", saves=get_saved_data())

@app.route('/search')
def search():
    return render_template(
        "search.html",
        saves=get_saved_data()
    )

@app.route('/save', methods=['POST'])
def save():
    response = make_response(redirect(url_for('search')))
    # dumps : dump string
    data = get_saved_data()
    data.update(dict(request.form.items()))
    response.set_cookie('character', json.dumps(data))
    return response

# debug=True: reload everytime we change the code and save it
app.run(debug=True, port=8000, host='0.0.0.0')