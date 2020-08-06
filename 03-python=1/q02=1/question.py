##
##  Programación en Python
##  ===========================================================================
##
##  Imprima la cantidad de registros por letra para la primera columna del 
##  archivo `data.csv`, ordenados alfabeticamente por la letra.
##
##  Rta/
##  A,8
##  B,7
##  C,5
##  D,6
##  E,14
##
##  >>> Escriba su codigo a partir de este punto <<<
archivo = open('data.csv','r').readlines()
 
A = [row[0] for row in archivo if row[0] == 'A']
B = [row[0] for row in archivo if row[0] == 'B']
C = [row[0] for row in archivo if row[0] == 'C']
D = [row[0] for row in archivo if row[0] == 'D']
E = [row[0] for row in archivo if row[0] == 'E']
AA=str(len(A))
BB=str(len(B))
CC=str(len(C))
DD=str(len(D))
EE=str(len(E))
print('A,'+AA)
print('B,'+BB)
print('C,'+CC)
print('D,'+DD)
print('E,'+EE)

