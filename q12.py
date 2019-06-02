##
## Imprima la suma de la columna 2 por cada letra 
## de la columna 4, ordnados alfabeticamente.
##
## a,114
## b,40
## c,91
## d,65
## e,79
## f,110
## g,35
##
import csv
with open('data3.csv', 'r') as f:
    f = csv.reader(f, delimiter=',')#, quoting=csv.QUOTE_NONNUMERIC
    letras={}
    for r in f:
        letra=r[3].split(';')
        for l in letra:  
            existe=False            
            for x in letras:
                if(x==l):
                    existe=True
            if existe==True:
                valor=int(r[1])+int(letras[l])
            else:
                valor=r[1]
            letras[l]=valor
    for letra in sorted(letras):
        print (letra+","+str(letras[letra]))