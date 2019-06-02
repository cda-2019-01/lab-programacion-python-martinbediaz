##
## Genere una lista de tuplas, donde cada tupla contiene en la primera 
## posicion, el valor de la segunda columna; la segunda parte de la 
## tupla es una lista con las letras (ordenadas y sin repetir letra) 
## de la primera  columna que aparecen asociadas a dicho valor de la 
## segunda columna. Esto es:
##
## ('0', ['C'])
## ('1', ['A', 'B', 'D', 'E'])
## ('2', ['A', 'D', 'E'])
## ('3', ['A', 'B', 'D', 'E'])
## ('4', ['B', 'E'])
## ('5', ['B', 'C', 'D', 'E'])
## ('6', ['A', 'B', 'C', 'E'])
## ('7', ['A', 'C', 'D', 'E'])
## ('8', ['A', 'B', 'E'])
## ('9', ['A', 'B', 'C', 'E'])
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
        tupla=letra,sorted(list(set(letras[letra])))
        print (tupla)