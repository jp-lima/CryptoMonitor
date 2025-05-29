import pandas as pd; 
from pesquisa_binaria import pesquisa_de_criptomoedas
'''
dataframe_das_criptomoedas = pd.read_csv('cripto_em_ordem_alfabetica.csv')
df_copia = dataframe_das_criptomoedas
'''
pesquisa_usuario = 'h'.lower()



resultado_pesquisa = pesquisa_de_criptomoedas('cripto_em_ordem_alfabetica.csv', pesquisa_usuario )

print(resultado_pesquisa)


