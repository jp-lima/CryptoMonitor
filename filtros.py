import pandas as pd; 
from pesquisa_binaria import pesquisa_de_criptomoedas 


#Moeda,Preço,,,


dataframe_das_criptomoedas = pd.read_csv('cripto_em_ordem_alfabetica.csv')



pesquisa_usuario = 'hi'.lower()

resultado_pesquisa = pesquisa_de_criptomoedas('cripto_em_ordem_alfabetica.csv', pesquisa_usuario )



def criar_dicionario_com_valores_da_cripto(criptos_e_cordenadas, dataframe):
    lista = list()

    for itens in criptos_e_cordenadas[1]:

        dicionario_com_valores_criptos = {'Moeda': dataframe.iloc [itens]["Moeda"], 'Preço': dataframe.iloc[itens]["Preço"], "Volume":dataframe.iloc[itens]['Volume em 24 h']
    , "Capitalização": dataframe.iloc[itens]['Capitalização de mercado'], "FDV": dataframe.iloc[itens]['FDV']}
        lista.append(dicionario_com_valores_criptos)
    return lista






class Cripto():
    def __init__(self,dicionario_com_todos_os_valores__da_cripto, confirm_filtro, dicionario_com_valores_de_min_ou_max):  #função para definir quais foram os filtros pedidos

        #self.nome = dicionario_com_todos_os_valores__da_cripto['Moeda']

        self.min_max = dicionario_com_valores_de_min_ou_max

        self.lista_com_as_opcs = ['Preço', 'Volume', 'Capitalização', "FDV"]

        self.dicionario = dicionario_com_todos_os_valores__da_cripto
        self.lista_com_as_opcs_escolhidas = list()
        
        for indice in range(0,4):
            if confirm_filtro[indice] == '1':
                self.lista_com_as_opcs_escolhidas.append(self.lista_com_as_opcs[indice])


    def filtro(self):    # função para conferir se aquele valor do elemento respeita o valor minimo e maximo

        l = list()

        for elementos in self.lista_com_as_opcs:
            
            
            
            if elementos in self.lista_com_as_opcs_escolhidas:
                print ( self.dicionario[elementos])
                    


dici = criar_dicionario_com_valores_da_cripto(resultado_pesquisa, dataframe_das_criptomoedas)

dicionario_valores_min_max = {'Preço': [0.5,0.9] , 'Volume': [889947, 12046162], 'Capitalização': [7081888,514775291], 'FDV': [7686909, 274248767]}

criptomoeda = Cripto(dici[0], '1101', dicionario_valores_min_max)

criptomoeda.filtro()



