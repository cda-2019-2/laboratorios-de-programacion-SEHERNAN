##
##  Programación en Python
##  ===========================================================================
##
##  Para el archivo `data.csv`, imprima una tabla en formato CSV que contenga 
##  por registro, la letra de la columna 1 y la cantidad de elementos de las 
##  columnas 4 y 5. 
## 
##  Rta/
##  E,3,5
##  A,3,4
##  B,4,4
##  ...
##  C,4,3
##  E,2,3
##  E,3,3
##
##  >>> Escriba su codigo a partir de este punto <<<
f = open('data.csv','r')
 
lista = []
temporal = []
 
for line in f:
    y=line.strip()
    z=y.split()
    lista.append(z)
 
for line in range(len(lista)):
    temporal.append([lista[line][0],lista[line][3].count(',')+1,lista[line][4].count(',')+1])
 
for line in range(len(temporal)):
    print(temporal[line][0],',',temporal[line][1],',',temporal[line][2],sep='') 



