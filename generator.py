#!/usr/bin/python3
import os
import requests
import shutil
from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def main():
    """renders the main page"""
    return render_template("index.html")


@app.route('/contact')
def contact():
    """contact page route"""
    return render_template("contact.html")


@app.route('/generate', methods=['POST'])
def generate():
    """generate the image according to user input"""
    width = int(request.form['width'])
    height = int(request.form['height'])
    category = 'nature'
    category = request.form['category']
    print(width, height, category)

    api_url = 'https://api.api-ninjas.com/v1/randomimage?category={}&width={}&height={}'.format(category, width, height)

    response = requests.get(api_url, headers={'X-Api-Key': 'HYGY2cz08gKZ60704/x3rg==8LkLqGiVtG8C24FX', 'Accept': 'image/jpg'}, stream=True)

    # Create the 'static' directory if it doesn't exist
    static_dir = os.path.join(os.path.dirname(__file__), 'static')
    os.makedirs(static_dir, exist_ok=True)

    if response.status_code == requests.codes.ok:
        with open(os.path.join(static_dir, 'img.jpg'), 'wb') as out_file:  # Save the image in the 'static' folder
            shutil.copyfileobj(response.raw, out_file)
        return render_template("index.html", image_url='static/img.jpg')
    else:
        return "Error: {} {}".format(response.status_code, response.text)

@app.route('/coming_soon')
def coming_soon():
    """Coming soon page route"""
    return render_template("coming_soon.html")


if __name__ == '__main__':
    app.run(debug=True)
