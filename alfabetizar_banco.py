import pandas as pd; from itertools import chain
from objeto import *
nomes = list()
df = pd.DataFrame()

#função para separar os nomes das criptos em listas que estão em ordem alfabetica
def organizar_na_ordem_por_lista (nome_dataframe):                
    
    #variaveis de configuração{
    df_das_criptos = pd.read_csv(nome_dataframe) 
    nome_desordenado_das_criptos=list()
    lista_de_A_a_Z = [['Aa'],['Bb'], ['Cc'], ['Dd'], ['Ee'], ['Ff'], ['Gg'], ['Hh'], ['Ii'], ['Jj'], ['Kk'], ['Ll'],['Mm'], ['Nn'], ['Oo'],['Pp'], ['Qq'], ['Rr'], 
['Ss'], ['Tt'], ['Uu'], ['Vv'],['Ww'], ['Xx'], ['Yy'], ['Zz'] ]
    #}

    #pegar todos os nomes das criptos do dataframe e adicionar numa lista
    for linhas in df_das_criptos.index:  
        nome = df_das_criptos.loc[linhas,'Moeda']
        nome_desordenado_das_criptos.append(nome)

    
    for nome_cada_cripto in nome_desordenado_das_criptos:
        for lista_alfabetica in lista_de_A_a_Z:

            if nome_cada_cripto[0] in lista_alfabetica[0]:
                lista_alfabetica.append(nome_cada_cripto)
                break
        else:
            lista_de_A_a_Z.append([nome_cada_cripto])

    lista_ordem_alfabetica_definitiva = organizar_em_ordem_alfabetica_dentro_das_listas(lista_de_A_a_Z)
    return lista_ordem_alfabetica_definitiva


def organizar_em_ordem_alfabetica_dentro_das_listas(lista):   #função para organizar a ordem dos nomes dentro de suas respectivas listas
    lista_mais_ordenada = list()
    cont = 0
    for listas in lista:
        cont += 1
        ordenado= sorted(listas, key=str.lower)
        lista_mais_ordenada.append(ordenado)
    return lista_mais_ordenada

# A função de criar df da classe Cripto só identifica indices, é preciso transformar toda a lista com criptos em uma lista com indice

def transformar_listas_de_nome_em_lista_de_indice(lista_com_nomes_em_ordem_alfabetica,df, lista_todos_indices):

    # variaveis de configuração {
    lista = lista_com_nomes_em_ordem_alfabetica[0]
    nome_duma_cripto_na_lista = lista[0]
        #}

    lista_com_nomes_em_ordem_alfabetica = list(chain.from_iterable(lista_com_nomes_em_ordem_alfabetica))
    
    for nome_duma_cripto_na_lista in lista_com_nomes_em_ordem_alfabetica:
        for linha in df.index:
            nome_duma_cripto_no_df = df.loc[linha, 'Moeda']
            
            if nome_duma_cripto_na_lista == nome_duma_cripto_no_df:
                df.drop(linha,axis=0)
                df = df.reset_index(drop=True)
                lista_todos_indices.append(linha)

    return lista_todos_indices

# controlar todas as funções
def alfabetizar_tudo():
    df = pd.read_csv('banco_de_dados/criptomoedas.csv')
    df_outro = pd.DataFrame()
    lista = list()
    criptomoeda_objeto = Cripto(df)
    #}
    listinha = organizar_na_ordem_por_lista('banco_de_dados/criptomoedas.csv')
    lista_indices  = transformar_listas_de_nome_em_lista_de_indice(listinha,df, lista)

    for indice in lista_indices:
        df_outro = criptomoeda_objeto.criar_dataframe_numa_linha(indice, df_outro)
        df_qua = df_outro.reset_index(drop=True)

    df_qua.to_csv('banco_de_dados/cripto_em_ordem_alfabetica.csv', index=False)


alfabetizar_tudo()



