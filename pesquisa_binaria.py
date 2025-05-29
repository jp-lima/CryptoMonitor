import pandas as pd


pesquisa_usuario = 'i'.lower()




def pesquisador (nome_dataframe, nome_da_cripto, lista_cordenadas):
    
    dataframe = pd.read_csv(nome_dataframe)
    #df_copia = dataframe
    
    baixo = 0
    alto = len (dataframe)  - 1
    while baixo <= alto:
        meio = (baixo + alto) // 2
        while meio in lista_cordenadas:
            meio += 1 
            
        if meio > alto:
            return None
        
        ch = dataframe.loc [meio, "Moeda"]
        chute = ch.lower()
        
        if chute [0:len(nome_da_cripto)] == nome_da_cripto:
            dataframe.drop(meio, axis=0, inplace=True) #apagar o objeto encontrado do dataframe pra não ser encontrado duas vezes
            return ch,meio
            
        elif chute > nome_da_cripto:
            alto = meio - 1
            
        elif chute < nome_da_cripto:
            baixo = meio + 1
        
    return None



def pesquisa_de_criptomoedas(ndataframe, cripto):

    lista_cordenadas_criptomoedas_encontradas= []
    lista_criptomoedas_encontradas = []
    while True:    
        
    
        resultado = pesquisador (ndataframe, cripto, lista_cordenadas_criptomoedas_encontradas)
        
        if resultado == None:
            break
        
        lista_cordenadas_criptomoedas_encontradas.append(resultado[1])
        
        lista_criptomoedas_encontradas.append(resultado[0])

        #dataframe.drop(resultado[1], axis=0, inplace=True)
    return lista_criptomoedas_encontradas


#resultado_pesquisa = pesquisa_de_criptomoedas('cripto_em_ordem_alfabetica.csv', pesquisa_usuario )

