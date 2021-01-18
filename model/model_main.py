from flask import Flask
model_app = Flask(__name__)

@model_app.route('/')
def index():
    return 'Hello, People!'

if __name__ == "__main__":
    model_app.run()