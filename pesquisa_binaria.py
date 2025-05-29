import pandas as pd

dataframe_das_criptomoedas = pd.read_csv('cripto_em_ordem_alfabetica.csv')
df_copia = dataframe_das_criptomoedas

pesquisa_usuario = 'i'.lower()



lista_cordenadas_criptomoedas_encontradas= []

lista_criptomoedas_encontradas = []


def pesquisador (dataframe, nome_da_cripto):

    baixo = 0
    alto = len (dataframe)  - 1
    while baixo <= alto:
        meio = (baixo + alto) // 2
        while meio in lista_cordenadas_criptomoedas_encontradas:
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



def pesquisa_de_criptomoedas(dataframe, cripto):
    while True:    
        
        resultado = pesquisador (dataframe, cripto)
        
        if resultado == None:
            break
        
        lista_cordenadas_criptomoedas_encontradas.append(resultado[1])
        
        lista_criptomoedas_encontradas.append(resultado[0])

        dataframe.drop(resultado[1], axis=0, inplace=True)
    return lista_criptomoedas_encontradas


resultado_pesquisa = pesquisa_de_criptomoedas(df_copia, pesquisa_usuario )

print (resultado_pesquisa)