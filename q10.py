##
## Imprima una tabla en formato CSV que contenga por cada clave 
## de la columna 5, la correspondiente cantidad de registros 
## asociados (filas en el archivo)
##
## aaa,13
## bbb,16
## ccc,23
## ddd,23
## eee,15
## fff,20
## ggg,13
## hhh,16
## iii,18
## jjj,18
##
##
import csv
with open('data3.csv', 'r') as f:
    f = csv.reader(f, delimiter=',')#, quoting=csv.QUOTE_NONNUMERIC
    letras={}
    for r in f:
        lineas=r[4].split(';')
        for l in lineas:
            valores=l.split(':')
            ya_esta=False 
            for letra in letras.keys():             
                if(letra==valores[0]):
                    ya_esta=True
                    aux=letras[valores[0]]+1
                    letras[valores[0]]=aux                     
            if (ya_esta==False):
                letras[valores[0]]=1                   
    for letra in sorted(letras):
        print (letra+","+str(letras[letra]))