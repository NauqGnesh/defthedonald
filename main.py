from flask import Flask, redirect, render_template, send_from_directory, request
import os
import twitter.api

app = Flask(__name__)

root_dir = os.path.dirname(os.getcwd())


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/static/<path:path>')
def static_file(path):
    return send_from_directory('static', path)


@app.route('/api')
def api():
    return "You're now in the API! I am your master and you pickles shall do my bidding!"


@app.route('/login')
def login():
    return "You can't log in because you're not worthy"

@app.route('/tweet', methods=['GET', 'POST'])
def tweet():
    if request.method == 'POST':
        tweet_text = request.form['twitterStatus']
        twitter.api.post_tweets(tweet_text)
    return render_template('twitter.html') 

if __name__ == "__main__":
    app.run(debug=True)
