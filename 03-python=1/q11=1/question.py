##
##  Programación en Python
##  ===========================================================================
##
##  Para el archivo `data.csv`, imprima la suma de la columna 2 para cada 
##  letra de la columna 4, ordnados alfabeticamente.
##
##  Rta/
##  a,114
##  b,40
##  c,91
##  d,65
##  e,79
##  f,110
##  g,35
##
##  >>> Escriba su codigo a partir de este punto <<<
f = open('data.csv','r')
 
lista = []
 
#ingreso los registros a una lista para leerlos por linea
for line in f:
    y=line.strip()
    z=y.split()
    lista.append(z)
 
#Busco la existencia del caracter y luego guardo el valor de la columna 2 en una lista
a = []
for line in range(len(lista)):
    
    if lista[line][3].count('a') > 0:
        a.append(int(lista[line][1]))
 
b = []
for line in range(len(lista)):
    if lista[line][3].count('b') > 0:
        b.append(int(lista[line][1]))
 
c = []
for line in range(len(lista)):
    if lista[line][3].count('c') > 0:
        c.append(int(lista[line][1]))
 
d = []
for line in range(len(lista)):
    if lista[line][3].count('d') > 0:
        d.append(int(lista[line][1]))
 
e = []
for line in range(len(lista)):    
    if lista[line][3].count('e') > 0:
        e.append(int(lista[line][1]))
 
f = []
for line in range(len(lista)):
    if lista[line][3].count('f') > 0:
        f.append(int(lista[line][1]))
 
g = []
for line in range(len(lista)):
    if lista[line][3].count('g') > 0:
        g.append(int(lista[line][1]))
 
print('a,',sum(a),sep='')
print('b,',sum(b),sep='')
print('c,',sum(c),sep='')
print('d,',sum(d),sep='')
print('e,',sum(e),sep='')
print('f,',sum(f),sep='')
print('g,',sum(g),sep='')

