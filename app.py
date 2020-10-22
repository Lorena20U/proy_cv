from flask import Flask, request, redirect, url_for
from jinja2 import Template, Environment, FileSystemLoader
import yaml

file_loader = FileSystemLoader('templates')
env = Environment(loader = file_loader)

app = Flask(__name__)
with open('data.yml') as yaml_file:
    my_yaml = yaml.load(yaml_file)
    print(my_yaml)

def mensaje():
    mensaje = 'Hola desde el metodo.'
    return "alert('" + mensaje + "')"

@app.route('/')
def index():
    template = env.get_template('base.html')
    image_file = url_for('static', filename = my_yaml['fotografia'])
    title = my_yaml['informacion_pagina']['titulo']
    pers = my_yaml['informacion_personal']
    return template.render(my_data = my_yaml, image_file=image_file, title=title, pers=pers)

@app.route('/cv')
def cv():
    template = env.get_template('cv.html')
    image_file = url_for('static', filename = my_yaml['fotografia'])
    title = my_yaml['informacion_pagina']['titulo']
    pers = my_yaml['informacion_personal']
    idi = my_yaml['informacion_personal']['Idiomas']
    inter = my_yaml['informacion_personal']['Intereses']
    tecs = my_yaml['informacion_profesional']['tecnologias']
    links = my_yaml['informacion_redes']
    return template.render(my_data = my_yaml, image_file=image_file, title=title, pers=pers, idi = idi, inter=inter, tecs=tecs, links=links)

@app.route('/Linktree')
def linktree():
    template = env.get_template('home.html')
    image_file = url_for('static', filename = my_yaml['fotografia'])
    title = my_yaml['informacion_pagina']['titulo']
    pers = my_yaml['informacion_personal']
    links = my_yaml['informacion_redes']
    return template.render(my_data = my_yaml, image_file=image_file, title=title, pers=pers, links=links)

@app.route('/Contacto')
def contacto():
    template = env.get_template('contacto.html')
    image_file = url_for('static', filename = my_yaml['fotografia'])
    title = my_yaml['informacion_pagina']['titulo']
    pers = my_yaml['informacion_personal']
    co = my_yaml['informacion_contacto']
    return template.render(my_data = my_yaml, image_file=image_file, title=title, pers=pers, co=co)

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug = True)