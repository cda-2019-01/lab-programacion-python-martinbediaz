##
## Imprima por cada fila, la columna 1 y la suma de los valores
## de la columna 5
##
## E,22
## A,14
## B,14
## ....
## C,8
## E,11
## E,16
##
import csv
with open('data3.csv', 'r') as f:
    f = csv.reader(f, delimiter=',')#, quoting=csv.QUOTE_NONNUMERIC
    for r in f:
        letra=r[4].split(';')
        cont=0
        for l in letra:  
            valor=l.split(':')
            cont+=int(valor[1])
        print(r[0]+','+str(cont))