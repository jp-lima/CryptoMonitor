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
    
    def tratar_os_numeros_das_criptos(self,valor):  #no csv os numeros vem com pontos demais, virgulas, cifrão e 'US' tudo isso tem que ser tirado, e transformar em floar
        
        string_intermediario = str()

        for numero in valor:
            if numero.isnumeric():
                string_intermediario = string_intermediario + numero
            elif numero == ',':
                string_intermediario = string_intermediario + '.'
        
        if len(string_intermediario) < 5:
            return 0 

        valor_final = float(string_intermediario)

        return valor_final




    def filtrador(self,dataframe_criado_com_pesquisa, confirm_filtro, dicionario_com_valores_de_min_ou_max):    # função para conferir se aquele valor do elemento respeita o valor minimo e maximo
        # Variavéis de configuração {
        lista_com_as_opcs_d_filtro_escolhida = list()
        lista_com_as_opcs_possiveis_d_filtro = ['Preço','Volume em 24 h','Capitalização de mercado', "FDV"]
        qtd_de_filtros_respeitados_por_cripto = int()
        dicionario_c_indice_e_filtros_respeitados = dict()
        lista_com_os_dict = list()
        #           }

        # Verificar quais opções de filtros foram pedidos
        for indice,item in enumerate(lista_com_as_opcs_possiveis_d_filtro):
            if confirm_filtro[indice] == '1':
                lista_com_as_opcs_d_filtro_escolhida.append(item)
        #       )

        for index_dataframe in dataframe_criado_com_pesquisa.index: 
            
            for indice, opc_escolhida in enumerate(lista_com_as_opcs_d_filtro_escolhida):

                um_valor_da_cripto = self.tratar_os_numeros_das_criptos(dataframe_criado_com_pesquisa.loc[index_dataframe, opc_escolhida])
                valor_min = dicionario_com_valores_de_min_ou_max[opc_escolhida][0]
                valor_max = dicionario_com_valores_de_min_ou_max[opc_escolhida][1]

                if valor_min < um_valor_da_cripto < valor_max:
                    #print (dataframe_criado_com_pesquisa.loc[index_dataframe,"Moeda"], um_valor_da_cripto, opc_escolhida)
                    qtd_de_filtros_respeitados_por_cripto += 1

            #print (index_dataframe, qtd_de_filtros_respeitados_por_cripto)
            dicionario_c_indice_e_filtros_respeitados={'index': index_dataframe, 'filtros_respeitados': qtd_de_filtros_respeitados_por_cripto}
            lista_com_os_dict.append(dicionario_c_indice_e_filtros_respeitados)

            qtd_de_filtros_respeitados_por_cripto = 0

        return lista_com_os_dict

