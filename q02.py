##
## Imprima la cantidad de registros por letra para la 
## primera columna, ordenados alfabeticamente.
##
## A,8
## B,7
## C,5
## D,6
## E,14
##
#import pandas as pd
#import numpy as np
#df = pd.read_csv("data2.csv", header=None, sep=";")
#print(df.groupby(0)[0].count())
import csv
letras={}
with open('data3.csv', 'r') as f:
    f = csv.reader(f, delimiter=',')#, quoting=csv.QUOTE_NONNUMERIC
    letras={}
    for r in f:
        cont=1
        for z in r: 
            if(cont==1):
                ya_esta=False
                for valor in letras.keys():
                    if (valor==z):
                        ya_esta=True
                        aux=letras[valor]+1
                        letras[valor]=aux
                        
                if ya_esta==False:
                    letras[z]=1          
            cont+=1
    for letra in sorted(letras):
        print (letra+","+str(letras[letra]))