import pandas as pd
from objeto import *


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
    dataframe_com_resultado = pd.DataFrame()
    

    lista_cordenadas_criptomoedas_encontradas= []
    lista_criptomoedas_encontradas = []
    while True:    
        
        dataframe = dataframe.reset_index(drop=True)

        resultado = pesquisador (dataframe, cripto)
        

        print (resultado)
        
        if resultado == None:
            break
        else:
            criptomoeda_objeto =  Cripto(dataframe)
            dataframe_com_resultado = criptomoeda_objeto.criar_dataframe_numa_linha(resultado[1],dataframe_com_resultado )
            dataframe.drop(resultado[1], axis=0, inplace=True)
        lista_cordenadas_criptomoedas_encontradas.append(resultado[1])
        
        lista_criptomoedas_encontradas.append(resultado[0])
        #lista_criptomoedas_encontradas,lista_cordenadas_criptomoedas_encontradas
    dataframe_com_resultado = dataframe_com_resultado.reset_index(drop=True)
    return dataframe_com_resultado




if __name__ == "__main__":
    criptomoeda_objeto = Cripto('banco_de_dados/cripto_em_ordem_alfabetica.csv')

    
    df = pd.DataFrame()
    pesquisa_usuario = 'pa'.lower()
    resultado_pesquisa = pesquisa_de_criptomoedas('banco_de_dados/cripto_em_ordem_alfabetica.csv', pesquisa_usuario )
    
    print (resultado_pesquisa)
    
