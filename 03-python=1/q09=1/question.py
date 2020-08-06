##
##  Programación en Python
##  ===========================================================================
##
##  Para el archivo `data.csv, imprima una tabla en formato CSV que contenga 
##  la cantidad de registros en que aparece cada clave de la columna 5.
##
##  Rta/
##  aaa,13
##  bbb,16
##  ccc,23
##  ddd,23
##  eee,15
##  fff,20
##  ggg,13
##  hhh,16
##  iii,18
##  jjj,18
##
##  >>> Escriba su codigo a partir de este punto <<<
f = open('data.csv','r')
 
lista = []
 
countaaa = 0
countbbb = 0
countccc = 0
countddd = 0
counteee = 0
countfff = 0
countggg = 0
counthhh = 0
countiii = 0
countjjj = 0
 
for line in f:
    x=line.replace(',',' ')
    x=x.replace(':',' ')
    y=x.strip()
    z=y.split()
 
  
    lista.append(z[3:])
#print(lista)
 
for i in range(len(lista)):
    for j in range(len(lista[i])-1):
        if lista[i][j] == ('aaa'):
            countaaa += 1
        elif lista[i][j] == ('bbb'):
            countbbb += 1
        elif lista[i][j] == ('ccc'):
            countccc += 1
        elif lista[i][j] == ('ddd'):
            countddd += 1
        elif lista[i][j] == ('eee'):
            counteee += 1
        elif lista[i][j] == ('fff'):
            countfff += 1
        elif lista[i][j] == ('ggg'):
            countggg += 1
        elif lista[i][j] == ('hhh'):
            counthhh += 1
        elif lista[i][j] == ('iii'):
            countiii += 1
        elif lista[i][j] == ('jjj'):
            countjjj += 1
 
print('aaa,',countaaa,sep='')
print('bbb,',countbbb,sep='')
print('ccc,',countccc,sep='')
print('ddd,',countddd,sep='')
print('eee,',counteee,sep='')
print('fff,',countfff,sep='')
print('ggg,',countggg,sep='')
print('hhh,',counthhh,sep='')
print('iii,',countiii,sep='')
print('jjj,',countjjj,sep='')




