##
## Imprima la cantidad de registros por cada mes.
##
## 01,3
## 02,4
## 03,2
## 04,4
## 05,3
## 06,3
## 07,5
## 08,6
## 09,3
## 10,2
## 11,2
## 12,3
##
import csv
letras={}
with open('data3.csv', 'r') as f:
    f = csv.reader(f, delimiter=',')#, quoting=csv.QUOTE_NONNUMERIC
    letras={}
    for r in f:
        fecha=r[2].split('-')
        #print()        
        ya_esta=False
        for valor in letras.keys():
            if (valor==fecha[1]):
                ya_esta=True
                aux=int(letras[valor]) + 1
                letras[valor]=aux       
        if ya_esta==False:
            letras[fecha[1]]=1
                   
    for letra in sorted(letras):
        print (letra+","+str(letras[letra]))
