import os 
from dotenv import load_dotenv
import tweepy

# To set your enviornment variables in your terminal run the following line or put them in a .env file:
# export 'CONSUMER_KEY'='<your_consumer_key>'
# export 'CONSUMER_SECRET'='<your_consumer_secret>'
# export 'ACCESS_TOKEN'='<your_access_token>'
# export 'ACCESS_TOKEN_SECRET'='<your_access_token_secret>'
load_dotenv()

consumer_key = os.environ.get("CONSUMER_KEY")
consumer_secret = os.environ.get("CONSUMER_SECRET")
access_token= os.environ.get("ACCESS_TOKEN")
access_token_secret = os.environ.get("ACCESS_TOKEN_SECRET")

auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api=tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
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

