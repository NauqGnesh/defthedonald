from flask import Flask, redirect, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/api')
def api():
    return "You're now in the API!"

@app.route('/home')
def homepage():
    return render_template('hello.html')