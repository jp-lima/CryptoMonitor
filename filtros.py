import pandas as pd; 
from pesquisa_binaria import pesquisa_de_criptomoedas 


#Moeda,Preço,,,


dataframe_das_criptomoedas = pd.read_csv('cripto_em_ordem_alfabetica.csv')



pesquisa_usuario = 'hi'.lower()

resultado_pesquisa = pesquisa_de_criptomoedas('cripto_em_ordem_alfabetica.csv', pesquisa_usuario )



def criar_dicionario_com_valores_da_cripto(criptos_e_cordenadas, dataframe):
    lista = list()

    for itens in criptos_e_cordenadas[1]:

        dicionario_com_valores_criptos = {'Moeda': dataframe.iloc [itens]["Moeda"], 'Preço': dataframe.iloc[itens]["Preço"], "Volume em 24h":dataframe.iloc[itens]['Volume em 24 h']
    , "Capitalização": dataframe.iloc[itens]['Capitalização de mercado'], "FDV": dataframe.iloc[itens]['FDV']}
        lista.append(dicionario_com_valores_criptos)
    return lista


t = criar_dicionario_com_valores_da_cripto(resultado_pesquisa, dataframe_das_criptomoedas)

print (t[1])







class Cripto():
    def __init__(self, nome, dicionario_com_todos_os_valores__da_cripto):
        self.nome = nome

        self.dicionario = dicionario_com_todos_os_valores__da_cripto

    def filtro(self, confirm_filtro, lista_valores_min_max):    # função para ver qual filtro foi pedido e se aquele valor do elemento respeita o valor minimo e maximo
        print ('nada')
        





def definir_filtros(nome, cordendas_das_criptos):
    cripto = Cripto()

    dataframe = pd.read_csv(nome)

    for cordenada in cordendas_das_criptos:
        

        nome_criptomoeda = dataframe.loc[cordenada, "Moeda"]
        
        cripto_objeto = Cripto(nome_criptomoeda, "0000")


        volume_em_24h_criptomoeda = dataframe.loc[cordenada, "Volume em 24 h"]
        capitalizacao_criptomoeda = dataframe.loc[cordenada, "Capitalização de mercado"]
        fdv_criptomoeda = dataframe.loc[cordenada, "FDV"]
        preco_criptomoeda = dataframe.loc[cordenada, "Preço"]

        filtro_preco = cripto_objeto.filtro(preco_criptomoeda)






