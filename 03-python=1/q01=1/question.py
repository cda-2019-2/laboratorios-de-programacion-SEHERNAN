##
##  Programación en Python
##  ===========================================================================
##
##  Imprima la suma de la segunda columna del archivo `data.csv`.
##
##  Rta/
##  190
##
##  >>> Escriba su codigo a partir de este punto <<<
archivo = open('data.csv','r')
columna2 = []
 
for line in archivo:
   x = line.strip()
   y = x.split()
   columna2.append(int(y[1]))
archivo.close()
print(sum(columna2))

