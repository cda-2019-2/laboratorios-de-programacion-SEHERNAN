##
##  Programación en Python
##  ===========================================================================
##
##  Para el archivo `data.csv`, imprima por cada fila, la columna 1 y la suma 
##  de los valores de la columna 5.
##
##  Rta/
##  E,22
##  A,14
##  B,14
##  ....
##  C,8
##  E,11
##  E,16
##
##  >>> Escriba su codigo a partir de este punto <<<
f = open('data.csv','r')
#listas temporales para extraer los datos
lista = []
temporal = []
temporal2 = []
temporal3 = []
temporal4 = []
#separar las claves con ':'
for line in f:
    
    x=line.replace(':',',: ')
    x=x.replace(',',' ')
    y=x.strip()
    z=x.split()
    
    lista.append(z)
#extraer la columna 5
for line in range(len(lista)):
    temporal.append(lista[line][4:])
for line in range(len(temporal)):
    temporal2.append(temporal[line])
#extraer los valores numericos de las claves
for i in range(len(temporal2)):
    for j in range(len(temporal2[i])):
        if temporal2[i][j] == ':':
            temporal3.append(int(temporal2[i][j+1]))
        
    temporal4.append(sum(temporal3))
    temporal3 = []
#suma de los valores numericos de las claves con su valor de la columna 0  
for line in range(len(lista)):
    print(lista[line][0],',',temporal4[line],sep='')



