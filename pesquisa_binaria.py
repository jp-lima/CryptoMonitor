import pandas as pd




def pesquisador (dataframe, nome_da_cripto):
    
    
    #df_copia = dataframe
    
    baixo = 0
    alto = len (dataframe)  - 1
    while baixo <= alto:
        meio = (baixo + alto) // 2
        #while meio in lista_cordenadas:
            #meio += 1 
            
        if meio > alto:
            return None
        
        ch = dataframe.iloc [meio]["Moeda"]

        chute = ch.lower()
        
        if chute [0:len(nome_da_cripto)] == nome_da_cripto:
        

            #dataframe.drop(meio, axis=0, inplace=True) #apagar o objeto encontrado do dataframe pra não ser encontrado duas vezes
            return ch,meio
            
        elif chute > nome_da_cripto:
            alto = meio - 1
            
        elif chute < nome_da_cripto:
            baixo = meio + 1
        
    return None



def pesquisa_de_criptomoedas(ndataframe, cripto):
    dataframe = pd.read_csv(ndataframe)
    lista_cordenadas_criptomoedas_encontradas= []
    lista_criptomoedas_encontradas = []
    while True:    
        
        dataframe = dataframe.reset_index(drop=True)

    
        resultado = pesquisador (dataframe, cripto,)

        
        if resultado == None:
            break
        else:
            dataframe.drop(resultado[1], axis=0, inplace=True)
        lista_cordenadas_criptomoedas_encontradas.append(resultado[1])
        
        lista_criptomoedas_encontradas.append(resultado[0])

        
    return lista_criptomoedas_encontradas,lista_cordenadas_criptomoedas_encontradas





'''

pesquisa_usuario = 'y'.lower()


resultado_pesquisa = pesquisa_de_criptomoedas('cripto_em_ordem_alfabetica.csv', pesquisa_usuario )
print (len (resultado_pesquisa[0]))
'''