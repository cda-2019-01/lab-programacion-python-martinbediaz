##
## Imprima la suma de la columna 2 por cada letra de la 
## primera columna, ordneados alfabeticamente.
##
## A,37
## B,36
## C,27
## D,23
## E,67
##
#import pandas as pd
#import numpy as np
#df = pd.read_csv("data2.csv", header=None, sep=";")
#df.groupby([0])[1].sum()
import csv
letras={}
with open('data3.csv', 'r') as f:
    f = csv.reader(f, delimiter=',')#, quoting=csv.QUOTE_NONNUMERIC
    letras={}
    for r in f:
        ya_esta=False
        for valor in letras.keys():
            if (valor==r[0]):
                ya_esta=True
                aux=int(r[1]) + int(letras[r[0]])
                letras[valor]=aux       
        if ya_esta==False:
            letras[r[0]]=r[1]
                   
    for letra in sorted(letras):
        print (letra+","+str(letras[letra]))