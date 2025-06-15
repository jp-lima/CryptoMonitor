import pandas as pd; 
from pesquisa_binaria import pesquisa_de_criptomoedas 
from objeto import *



dataframe_das_criptomoedas = pd.read_csv('banco_de_dados/cripto_em_ordem_alfabetica.csv')

pesquisa_usuario = 'bit'.lower()

resultado_pesquisa = pesquisa_de_criptomoedas('banco_de_dados/cripto_em_ordem_alfabetica.csv', pesquisa_usuario )

objeto = Cripto(dataframe_das_criptomoedas)




dicionario_valores_min_max = {'Preço': [0.5,0.9], 'Volume em 24 h': [889947, 12046162], 'Capitalização de mercado': [7081888,514775291], 'FDV': [7686909, 274248767]}


e = objeto.filtrador(resultado_pesquisa,'1001', dicionario_valores_min_max)


def filtro(dicionario_min_max,objeto, dici_resultado_pesquisa):
    #variaveis  de configuração
    lista_com_indices = list()
    df_filtrado= pd.DataFrame()
    lista_d_dicionario_com_os_filtros = objeto.filtrador(dici_resultado_pesquisa,'1111', dicionario_min_max)
    objeto_novo = Cripto(dici_resultado_pesquisa)
    #}


    for indice in range (0,5):
        for dicionarios in lista_d_dicionario_com_os_filtros:
            if dicionarios['filtros_respeitados'] == indice:

                lista_com_indices.append(dicionarios['index'])

    for indice_dos_filtrados in lista_com_indices:
        df_filtrado = objeto_novo.criar_dataframe_numa_linha(indice_dos_filtrados, df_filtrado)

    print(df_filtrado)
    



filtro(dicionario_valores_min_max,objeto,resultado_pesquisa)

