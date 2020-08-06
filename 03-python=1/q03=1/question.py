##
##  Programación en Python
##  ===========================================================================
##
##  Para el archivo `data.csv`, imprima la suma de la columna 2 por cada letra 
##  de la primera columna, ordneados alfabeticamente.
##
##  Rta/
##  A,37
##  B,36
##  C,27
##  D,23
##  E,67
##
##  >>> Escriba su codigo a partir de este punto <<<

archivo = open('data.csv','r').readlines()
 
#A = [[row[0],row[2]] for row in archivo if row[0] == 'A']
A2 = [int(str(row[2])) for row in archivo if row[0] == 'A']
 
#a2 = int(str(A2))
B2 = [int(str(row[2])) for row in archivo if row[0] == 'B']
C2 = [int(str(row[2])) for row in archivo if row[0] == 'C']
D2 = [int(str(row[2])) for row in archivo if row[0] == 'D']
E2 = [int(str(row[2])) for row in archivo if row[0] == 'E']
 
def sumalista(listaNumeros):
   laSuma = 0
   for i in listaNumeros:
       laSuma = laSuma + i
   return laSuma
 
print('A,'+(str(sumalista(A2))))
print('B,'+(str(sumalista(B2))))
print('C,'+(str(sumalista(C2))))
print('D,'+(str(sumalista(D2))))
print('E,'+(str(sumalista(E2))))

