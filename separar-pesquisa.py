import pandas as pd
nomes = list()

df_das_criptos = pd.read_csv('criptomoedas.csv') #Transformar o arquivo CSV em dataframe
cont = -1

for n in df_das_criptos.index:                            #pegar os nomes das criptos do dataframe e adicionar numa lista
    cont = cont + 1
    nome = df_das_criptos.loc[cont,'Moeda']
    nomes.append(nome)

df = pd.DataFrame()


ordem_alfabetica = [['Aa'],['Bb'], ['Cc'], ['Dd'], ['Ee'], ['Ff'], ['Gg'], ['Hh'], ['Ii'], ['Jj'], ['Kk'], ['Ll'],['Mm'], ['Nn'], ['Oo'],['Pp'], ['Qq'], ['Rr'], 
['Ss'], ['Tt'], ['Uu'], ['Vv'],['Ww'], ['Xx'], ['Yy'], ['Zz'] ]
{}

def transformar_cripto_em_dataframe(df, dicionario_das_criptos):
    criptos = pd.DataFrame(dicionario_das_criptos)
    return pd.concat([df,criptos], ignore_index=True)

def organizar_na_ordem (nome, lista_geral):                #função para separar os nomes das criptos em listas que estão em ordem alfabetica
    for n in lista_geral:
        if nome[0] in n[0]:
            n.append(nome)
            break
    else:
        lista_geral.append([nome])
    return lista_geral

def organizar_em_ordem_alfabetica_dentro_das_listas(lista):   #função para organizar os nomes das criptos dentro de suas respectivas listas
    lista_mais_ordenada = list()
    cont = 0
    for listas in lista:
        cont += 1
        ordenado= sorted(listas, key=str.lower)
        lista_mais_ordenada.append(ordenado)
    return lista_mais_ordenada

for m in nomes:
    lista_nova = organizar_na_ordem(m, ordem_alfabetica)     

lista_final = organizar_em_ordem_alfabetica_dentro_das_listas(lista_nova)
{}
dicionario_das_criptos = dict() 
#Moeda,Preço,Volume em 24 h,Capitalização de mercado,FDV,

lista_com_os_nomes=list()
lista_com_preço = list()
lista_com_o_volume = list()
lista_com_a_capitalização = list()
lista_com_o_fdv = list()

for alfabeto in lista_final:
    for nome_cripto in alfabeto:
        for n in df_das_criptos.index:
            if nome_cripto == df_das_criptos.loc[n, 'Moeda']:
                lista_com_os_nomes.append(nome_cripto)
                preço = df_das_criptos.loc[n,"Preço"]
                lista_com_preço.append(preço)
                volume_em_vinte_e_quatro_h = df_das_criptos.loc[n,"Volume em 24 h"]
                lista_com_o_volume.append(volume_em_vinte_e_quatro_h)
                capitalização = df_das_criptos.loc[n, "Capitalização de mercado"]
                lista_com_a_capitalização.append(capitalização)
                fdv = df_das_criptos.loc[n, "FDV"]
                lista_com_o_fdv.append(fdv)


dicionario_das_criptos = {'Moeda': lista_com_os_nomes ,'Preço': lista_com_preço,'Volume em 24 h':lista_com_o_volume,'Capitalização de mercado':lista_com_a_capitalização,'FDV':lista_com_o_fdv}

criptos = pd.DataFrame(dicionario_das_criptos)



print (criptos)

criptos.to_csv('cripto_em_ordem_alfabetica.csv', index=False)