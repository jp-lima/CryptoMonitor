import pandas as pd

t = pd.read_csv('criptomoedas.csv')


linha = t.iloc[2]



data = pd.DataFrame(linha)

print (data)