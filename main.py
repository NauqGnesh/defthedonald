from flask import Flask, redirect, render_template
import os

app = Flask(__name__)

root_dir = os.path.dirname(os.getcwd())


@app.route('/')
def hello_world():
    # print(os.path.join("~/Code/defthedonald/", 'index.html'))
    return render_template('index.html')


@app.route('/api')
def api():
    return "You're now in the API! I am your master and you pickles shall do my bidding!"


@app.route('/login')
def login():
    return "You can't log in because you're not worthy"


if __name__ == "__main__":
    app.run(debug=True)
