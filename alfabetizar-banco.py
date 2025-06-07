import pandas as pd
nomes = list()

df = pd.DataFrame()

class Cripto():
    def __init__(self, nome_dataframe):
        self.dataframe = pd.read_csv(nome_dataframe)
        
        #lista_com_todos_os_dicionarios_dos_valores_das_criptos.append(dicionario_com_valores_criptos)

    def criar_dataframe_numa_linha(self,indice,dataframe_existente):
        self.dicionario_com_valores_criptos = {'Moeda': self.dataframe.iloc [indice]["Moeda"], 'Preço': self.dataframe.iloc[indice]["Preço"]
    , "Volume":self.dataframe.iloc[indice]['Volume em 24 h'] , "Capitalização": self.dataframe.iloc[indice]['Capitalização de mercado'], "FDV": self.dataframe.iloc[indice]['FDV']}
        
        df_novo = pd.DataFrame([self.dicionario_com_valores_criptos])

        dt = pd.concat([df_novo, dataframe_existente])

        return dt



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


#lista_ordem_alfabetica_definitiva = organizar_em_ordem_alfabetica_dentro_das_listas(lista_nova)

def transformar_listas_de_nome_em_lista_de_indice(lista_com_nomes_em_ordem_alfabetica, nome_do_dataframe):
    lista_todos_indices = list()
    df = pd.read_csv(nome_do_dataframe)
    lista=['qualquer palavra, não importa']
    while len(lista_com_nomes_em_ordem_alfabetica) > 0:
        print (lista)
        df_copia = df.reset_index()
        
        if len(lista) == 0:
            del (lista_com_nomes_em_ordem_alfabetica[0])

        lista = lista_com_nomes_em_ordem_alfabetica[0]
        nome_de_uma_cripto = lista[0]

        for linha in df_copia.index:
            nome_da_cripto_q_esta_no_df = df.loc[linha, 'Moeda']

            if nome_da_cripto_q_esta_no_df == nome_de_uma_cripto:
                lista_todos_indices.append(linha)
                df.drop(linha, axis=0)
                del(lista[0])
    return lista_todos_indices


def alfabetizar_tudo():

    criptomoeda_objeto = Cripto('banco_de_dados/criptomoedas.csv')



    lista_com_todos_nomes_organizados = organizar_na_ordem_por_lista('banco_de_dados/criptomoedas.csv')
    

    lista_dos_nomes_por_letra = lista_com_todos_nomes_organizados[0]

    for criptomoeda in lista_dos_nomes_por_letra:
        criptomoeda_objeto.criar_dataframe_numa_linha()



deci = {
'Moeda': ['caralho', 'bitch'],
'Preço': ['ww33', 'tr555'],
'Volume': ['12.232.343','US 98388789'],
'Capitalização': ['US  65.426',  'US 454.766'],
'FDV': ['US 45.234', 'YER 976.876.988']
}


x = Cripto('banco_de_dados/criptomoedas.csv')

r = pd.DataFrame(deci)

d = x.criar_dataframe_numa_linha(12,r)

d = x.criar_dataframe_numa_linha(134,d)


d = d.reset_index(drop=True)

print (d)

listinha = organizar_na_ordem_por_lista('banco_de_dados/criptomoedas.csv')

lista_indices  = transformar_listas_de_nome_em_lista_de_indice(listinha, 'banco_de_dados/criptomoedas.csv')

print (lista_indices)