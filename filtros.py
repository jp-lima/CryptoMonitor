import pandas as pd; 
from pesquisa_binaria import pesquisa_de_criptomoedas 



def criar_dicionario_com_valores_da_cripto(criptos_e_cordenadas, dataframe):  #criar dicionario organizado com os valores de preço,fdv,volume e capitalização de cada criptomoeda
    lista_com_todos_os_dicionarios_dos_valores_das_criptos = list()

    for itens in criptos_e_cordenadas[1]:

        dicionario_com_valores_criptos = {'Moeda': dataframe.iloc [itens]["Moeda"], 'Preço': tratar_os_numeros_das_criptos(dataframe.iloc[itens]["Preço"])
, "Volume": tratar_os_numeros_das_criptos(dataframe.iloc[itens]['Volume em 24 h'])  , "Capitalização": tratar_os_numeros_das_criptos(dataframe.iloc[itens]['Capitalização de mercado']), "FDV": tratar_os_numeros_das_criptos(dataframe.iloc[itens]['FDV'])}
        lista_com_todos_os_dicionarios_dos_valores_das_criptos.append(dicionario_com_valores_criptos)
    
    return lista_com_todos_os_dicionarios_dos_valores_das_criptos


def tratar_os_numeros_das_criptos(valor):  #no csv os numeros vem com pontos demais, virgulas, cifrão e 'US' tudo isso tem que ser tirado, e transformar em floar
    
    string_intermediario = str()

    for indice in range(0,len(valor)):
        if valor[indice].isnumeric():
            string_intermediario = string_intermediario + valor[indice]
        elif valor[indice] == ',':
            string_intermediario = string_intermediario + '.'
    
    if len(string_intermediario) < 5:
        return 0 

    valor_final = float(string_intermediario)

    return valor_final






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


    def filtragem(self):    # função para conferir se aquele valor do elemento respeita o valor minimo e maximo

        l = list()

        for elementos in self.lista_com_as_opcs_escolhidas:
            print ( self.dicionario[elementos])



dataframe_das_criptomoedas = pd.read_csv('cripto_em_ordem_alfabetica.csv')

pesquisa_usuario = 'hi'.lower()

resultado_pesquisa = pesquisa_de_criptomoedas('cripto_em_ordem_alfabetica.csv', pesquisa_usuario )



dici = criar_dicionario_com_valores_da_cripto(resultado_pesquisa, dataframe_das_criptomoedas)


dicionario_valores_min_max = {'Preço': [0.5,0.9] , 'Volume': [889947, 12046162], 'Capitalização': [7081888,514775291], 'FDV': [7686909, 274248767]}








def filtros(lista_todas_criptos, lista_com_os_min_max, pedidos_filtro):
    objeto_criptomoeda = Cripto(dici[5], pedidos_filtro, lista_com_os_min_max)
    lista = list()
    for criptomoedas_com_valores in lista_todas_criptos:
        
        criptomoeda.filtragem()

#filtros (resultado_pesquisa[0], dicionario_valores_min_max,'1000')

print (dici)


