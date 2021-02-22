from flask import Flask, redirect, render_template, send_from_directory, request, url_for
import os
import twitter.api
from utils import Model
from model.model_main import index as generate_tweets

import tweepy

app = Flask(__name__)

tweets = {"tweet1", "tweet2"}

# Fetch model (synchronously for now)
Model.fetch()

# Log about model storage location
print("Model ostensibly stored at " + Model.get_path())

# Set configs
consumer_key = os.environ.get("CONSUMER_KEY")
consumer_secret = os.environ.get("CONSUMER_SECRET")
access_token= os.environ.get("ACCESS_TOKEN")
access_token_secret = os.environ.get("ACCESS_TOKEN_SECRET")

auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api=tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OKKk")
except:
    print("Error during authentication")


def post_tweets(tweet_text: str):
    """Post a tweet to twitter

    Args:
        tweet_text : str
            Tweet to be posted

    Returns:
        Error if POST requests fails
    """
    api.update_status(tweet_text)


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


@app.route("/post_tweet/<tweet>", methods=["GET"])
def post_tweet(tweet):
    if request.method == 'GET':
        """return the information for <tweet>"""
    twitter.api.post_tweets(tweet)
    return redirect(url_for('hello_world', tweets=tweets))

@app.route("/get_tweets/", methods=["POST"])
def get_tweets():
    tweets = generate_tweets()
    return redirect(url_for('hello_world', tweets=tweets))

if __name__ == "__main__":
    app.run(debug=True)
