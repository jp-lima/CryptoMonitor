from flask import Flask, render_template, request;
import pandas as pd
from pesquisa_binaria import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def resposta():
    moeda = request.form.get('pesquisa')
    print(moeda)

    resultado =  pesquisa_de_criptomoedas('banco_de_dados/cripto_em_ordem_alfabetica.csv',(moeda).lower())

    return render_template('output.html',nome_da_moeda= resultado )




if __name__ == '__main__':
    app.run(debug=True)