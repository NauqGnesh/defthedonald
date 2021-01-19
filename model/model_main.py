import model_loader
from flask import Flask
model_app = Flask(__name__)

@model_app.route('/')
def index():
    generation = model_loader.get_generations()
    print(generation)
    return generation[0]['generated_text']

if __name__ == "__main__":
    model_app.run()