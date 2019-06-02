import csv
with open('data3.csv', 'r') as f:
    f = csv.reader(f, delimiter=',')#, quoting=csv.QUOTE_NONNUMERIC
    ## se lee una linea a la vez
    cantidad=0
    for r in f:
        cont=1
        for z in r:
            if(cont==2):
                cantidad+=int(z)
            cont+=1
    print(cantidad)#import pandas as pd
#import numpy as np
#df = pd.read_csv("data2.csv", header=None, sep=";")
#print(df[1].sum())