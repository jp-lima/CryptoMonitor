import pandas as pd
dataframe_das_criptomoedas = pd.read_csv('cripto_em_ordem_alfabetica.csv')

df_copia = dataframe_das_criptomoedas

cripto = 'w'.lower()

cont = 0

llll= list()
t = str()
lista= list()

def pesquisando (dataframe, nome_da_cripto):
    baixo = 0
    alto = len (dataframe_das_criptomoedas)  - 1
    while baixo <= alto:
        meio = (baixo + alto) // 2
        while meio in llll:
            meio += 1 
            
        if meio > alto:
            return None
        
        ch = dataframe.loc [meio, "Moeda"]
        chute = ch.lower()
        
        if chute [0:len(nome_da_cripto)] == nome_da_cripto:
            return ch,meio
            
        elif chute > nome_da_cripto:
            alto = meio - 1
            
        elif chute < nome_da_cripto:
            baixo = meio + 1
        
    return None

cont = 0

while True:    
    t = pesquisando(df_copia, cripto)
    if t == None:
        break
    llll.append(t[1])
    lista.append(t[0])
    df_copia.drop(t[1], axis=0, inplace=True)
    print (lista)
    cont+= 1