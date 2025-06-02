from flask import Flask, render_template, request;
from filtros import *;


app = Flask(__name__)

app.route('/')
def index():
    return render_template('index.html', methods='POST')

app.route('/outputs')
def resposta():
    moeda = request.form.get('filtro_preço')

    min_max_preço = [request.form.get('min_preço'), request.form.get('max_preço')]

    



