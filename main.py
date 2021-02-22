from flask import Flask, redirect, render_template, send_from_directory
from utils import Model, APP_ROOT

app = Flask(__name__)

tweets = {"tweet1", "tweet2"}

# Fetch model (synchronously for now)
Model.fetch()


@app.route('/')
def hello_world():
    return render_template('index.html', tweets=tweets)


@app.route('/static/<path:path>')
def static_file(path):
    return send_from_directory('static', path)


@app.route('/api')
def api():
    return "You're now in the API! I am your master and you pickles shall do my bidding!"


@app.route('/login')
def login():
    return "You can't log in because you're not worthy"


if __name__ == "__main__":
    app.run(debug=True)
