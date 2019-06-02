##
## Por cada clave de la columna 5 (cadena de tres letras), obtenga
## el valor mas pequeño y el valor mas grande asociado a esa clave.
##
## aaa,0,6
## bbb,4,7
## ccc,0,1
## ddd,5,5
## eee,0,0
## fff,4,9
## ggg,3,3
## hhh,6,8
## iii,2,7
## jjj,2,5
##
import csv
with open('data3.csv', 'r') as f:
    f = csv.reader(f, delimiter=',')#, quoting=csv.QUOTE_NONNUMERIC
    letras={}
    for r in f:
        lineas=r[4].split(';')
        for l in lineas:
            valores=l.split(':')
            #print(valores)
            ya_esta=False 
            for letra in letras.keys():             
                if(letra==valores[0]):
                    ya_esta=True
                    if(valores[1] < letras[valores[0]][0]):
                        letras[valores[0]][0]=valores[1]
                    if(letras[valores[0]][1] < valores[1]):
                        letras[valores[0]][1]=valores[1]                       
            if (ya_esta==False):
                letras[valores[0]]=[valores[1],valores[1]]
                #print(letras[valores[0]])
                   
    for letra in sorted(letras):
        print (letra+","+str(letras[letra][0])+','+str(letras[letra][1]))