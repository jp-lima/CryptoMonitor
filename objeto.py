import pandas as pd


class Cripto():
    def __init__(self, dataframe):
        self.dataframe = dataframe

    def criar_dataframe_numa_linha(self,indice,dataframe_existente):

        self.dicionario_com_valores_criptos = {'Moeda': self.dataframe.iloc [indice]["Moeda"], 'Preço': self.dataframe.iloc[indice]["Preço"]
    , "Volume em 24 h":self.dataframe.iloc[indice]['Volume em 24 h'] , "Capitalização de mercado": self.dataframe.iloc[indice]['Capitalização de mercado'], "FDV": self.dataframe.iloc[indice]['FDV']}
        
        df_novo = pd.DataFrame([self.dicionario_com_valores_criptos])
        dt = pd.concat([dataframe_existente, df_novo,])

        return dt
    
    def filtragem(selfi,dataframe_criado_com_pesquisa, confirm_filtro, dicionario_com_valores_de_min_ou_max):    # função para conferir se aquele valor do elemento respeita o valor minimo e maximo
        lista_com_as_opcs_d_filtro_escolhida = list()
        lista_com_as_opcs_possiveis_d_filtro = ['Preço','Volume em 24 h','Capitalização de mercado', "FDV"]

        for indice,item in enumerate(lista_com_as_opcs_possiveis_d_filtro):
            if confirm_filtro[indice] == '1':
                lista_com_as_opcs_d_filtro_escolhida.append(item)
        
        for numero_das_linhas in dataframe_criado_com_pesquisa.index: 
            
            for numero, opc_escolhida in enumerate(lista_com_as_opcs_d_filtro_escolhida):

                um_valor_da_cripto = dataframe_criado_com_pesquisa.loc[numero_das_linhas, opc_escolhida]
                
                print (um_valor_da_cripto)




