import model_loader
from flask import Flask
model_app = Flask(__name__)

@model_app.route('/')
def index():
    generation = model_loader.get_generations()
    print(generation)
    generations = ""
    for g in generation:
        generations += g + "\n"
    return generations

if __name__ == "__main__":
    model_app.run()