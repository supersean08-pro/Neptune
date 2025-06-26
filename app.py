from flask import Flask, render_template, request
import os
from flask import render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/weight', methods=['GET', 'POST'])
def weight():
    weight = None
    mass = None
    distance = None
    equivalent_mass = None
    if request.method == 'POST':
        try:
            mass = float(request.form['mass'])
            distance = float(request.form['distance'])
            NEPTUNE_GRAVITY = 11.15 
            EARTH_GRAVITY = 9.81
            NEPTUNE_RADIUS = 24622000 #In Meters
            weight = mass * NEPTUNE_GRAVITY * distance / NEPTUNE_RADIUS
            equivalent_mass = weight / EARTH_GRAVITY
            weight = f"{weight:.2f}"
            equivalent_mass = f"{equivalent_mass:.2f}"
        except ValueError:
            weight = "Invalid input"
            equivalent_mass = None
    return render_template('weight.html', weight=weight, mass=mass, equivalent_mass=equivalent_mass)

@app.route('/voptions')
def voptions():
    return render_template('viewoptions.html')

@app.route('/scale')
def viewscale():
    return render_template('viewscale.html')

@app.route('/triton')
def viewtriton():
    return render_template('viewtriton.html')

@app.route('/credits')
def credits():
    return render_template('credits.html')

@app.route('/neptune')
def viewneptune():
    descriptions = {
        "surface": "The 'surface' is not solid — you'd float in thick methane clouds, seeing swirling blue storms and constant winds at supersonic speeds.",
        "atmosphere": "From the upper atmosphere, you'd see deep blues and purples, feeling pressure like 1,000 Earth atmospheres as you descend.",
        "triton": "Triton, Neptune’s moon, offers a frozen view of the planet, with Neptune’s stormy beauty dominating the sky in deep blue.",
        "orbit": "From orbit, Neptune appears calm, large, and distant — its faint ring system visible as a shimmering halo."
    }
    return render_template('viewneptune.html', descriptions=descriptions)

@app.route('/wiki')
def facts():
    return render_template('facts.html')

@app.route('/gallery')
def gallery():
    gallery_folder = os.path.join(app.static_folder, 'Gallery')
    image_files = [
        f'Gallery/{filename}'
        for filename in os.listdir(gallery_folder)
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.webp'))
    ]
    return render_template('gallery.html', image_files=image_files)

if __name__ == '__main__':
    app.run(debug=True)