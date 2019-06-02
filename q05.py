##
## Imprima el valor maximo y minimo por cada letra de la columa 1.
##
## A,9,1
## B,9,1
## C,9,0
## D,7,1
## E,9,1
##
import csv
letras={}
with open('data3.csv', 'r') as f:
    f = csv.reader(f, delimiter=',')#, quoting=csv.QUOTE_NONNUMERIC
    letras={}
    for r in f:
        #fecha=r[2].split('-')
        ya_esta=False
        for valor in letras.keys():
            if(valor==r[0]):
                ya_esta=True
                if(r[1]>letras[r[0]][0]):
                    letras[r[0]][0]=r[1]
                if(letras[r[0]][1] > r[1]):
                    letras[r[0]][1]=r[1]                    
                #aux=int(letras[valor]) + 1
                #letras[valor]=aux       
        if ya_esta==False:
            letras[r[0]]=[r[1],r[1]]
            #print(letras[r[0]])
                   
    for letra in sorted(letras):
        print (letra+","+str(letras[letra][0])+','+str(letras[letra][1]))
