
#Importando bibliotecas a serem utilizadas
import numpy as np
import datetime
import csv
import time

#Definindo variáveis fixas que serão utilizadas para serem geradas valores aleatórios
tags = ['Nivel_01.PV','Nivel_02.PV','Temperatura_01.PV', 'Temperatura_02.PV']
booleana = 0

while True:    
    if booleana == 0:
        diretorio = 'C:\Historian\Data\DataImport\FastLoad\dados.csv' 
        booleana = 1
    else:
        diretorio = 'C:\Historian\Data\DataImport\FastLoad\dados1.csv'       
        booleana = 0

    time.sleep(1)

#Define variáveis dentro do loop para atualizarem seus valores, limpando valores antigos e também receberem valores novos
    atual = datetime.datetime.now()
    lista = [
        ['ASCII'],
        ['',''],
        ['ASB_ENG',1,'Server Local',10,1]]

    #Define um valor aleatório para cada tipo de variável para cada range específico
    for i in tags:
        if 'Nivel' in str(i):
            valor = np.random.randint(0,100)
        elif 'Temperatura' in str(i):
            valor = np.random.randint(100,130)
        else:
            valor = np.random.randint(0,130)

        #Gera uma lista temporária para gerar uma nova linha no csv e a coloca na lista global. 
        #Passa os valores de timestamp e valores aleatórios
        Lista_Temporaria = [i,0,str(datetime.date.today()).replace('-','/'),str(atual.strftime("%H:%M:%S")),1,str(valor),192]
        lista.append(Lista_Temporaria)

    #Escrevendo em um arquivo CSV
    with open(diretorio, 'w', newline='') as f:
        writer = csv.writer(f)

        # Escreve todas as linhas
        writer.writerows(lista)
        
