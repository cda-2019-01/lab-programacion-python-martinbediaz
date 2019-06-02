##
## Genere una lista de tuplas, donde cada tupla contiene en la primera 
## posicion, el valor de la segunda columna; la segunda parte de la 
## tupla es una lista con las letras de la primera columna que aparecen
## asociadas a dicho valor de la segunda columna. Esto es:
##
##    ('0', ['C'])
##    ('1', ['E', 'B', 'D', 'A', 'A', 'E'])
##    ('2', ['A', 'E', 'D'])
##    ('3', ['A', 'B', 'D', 'E', 'E'])
##    ('4', ['E', 'B'])
##    ('5', ['B', 'C', 'D', 'D', 'E', 'E', 'E'])
##    ('6', ['C', 'E', 'A', 'B'])
##    ('7', ['A', 'C', 'E', 'D'])
##    ('8', ['E', 'E', 'A', 'B'])
##    ('9', ['A', 'B', 'E', 'C'])
##
##
import csv
with open('data3.csv', 'r') as f:
    f = csv.reader(f, delimiter=',')#, quoting=csv.QUOTE_NONNUMERIC
    letras={}
    for r in f:
        lista=[r[0]]        
        ya_esta=False
        for valor in letras.keys():
            if (valor==r[1]):
                ya_esta=True
                letras[r[1]].append(r[0])
        if (ya_esta==False):
            letras[r[1]]=[0]
            letras[r[1]][0]=r[0]

    for letra in sorted(letras.keys()):#sorted
        tupla=letra,letras[letra]
        print (tupla)