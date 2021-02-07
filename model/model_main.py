import model_loader
from flask import Flask
model_app = Flask(__name__)

@model_app.route('/')
def index():
    num_samples = 50
    models_folder = "./model_files/"
    model_name = "10epochs2013-2020"
    # model_name = "3_epochs_distilgpt2_2021-01-25_01-11"
    # model_name = "2_epochs_distilgpt2_2021-01-25_01-11"
    # model_name = "1_epochs_distilgpt2_2021-01-29_21-00"
    generations = model_loader.get_generations(model_folder=models_folder + model_name, num_samples=num_samples)

    # print(generations)

    model_samples_folder = "./model_samples/"
    f = open(model_samples_folder + model_name + f"_{str(num_samples)}_examples.txt", "w")
    header = f"Showing {num_samples} sample generations for {model_name}"
    f.write(header + "\n~~~\n")
    generations_html = f"<h3>{header}</h3><ol type='1'>"
    for i, g in enumerate(generations):
        generations_html += f"<li>{g}</li>"
        f.write(f"({i+1}) {g}\n")
    generations_html += "</ol>"
    f.close()

    return generations_html

if __name__ == "__main__":
    model_app.run()