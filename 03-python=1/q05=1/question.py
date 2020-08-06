##
##  Programación en Python
##  ===========================================================================
##
##  Para el archivo `data.csv`, imprima el valor maximo y minimo de la columna
##  2 por cada letra de la columa 1.
##
##  Rta/
##  A,9,1
##  B,9,1
##  C,9,0
##  D,7,1
##  E,9,1
##
##  >>> Escriba su codigo a partir de este punto <<<
import csv
from itertools import groupby
from operator import itemgetter

with open('data.csv') as fin, open('newfile.csv', 'w') as fout:
    for line in fin:
        fout.write(line.replace('\t', ','))
items = [] 
with open('newfile.csv') as File:
    reader = csv.reader(File, delimiter=',')
    for row in reader:
        items.append(row)

column1, column2, column3, column4 , column5 = [], [], [], [] ,[]

for i  in range(0, len(items)):
    column1.append(items[i][0])
    column2.append(items[i][1])
    column3.append(items[i][2])
    column4.append(items[i][3])
    column5.append(items[i][4])

        
column2 = [int(i) for i in column2] 


popo= sorted(list(set(column1)))
diccionario={}
for i in popo:
    lista=[]
    for j in range(len(column1)):
        if column1[j]==i:
            lista.append(column2[j])
    print(i+','+str(max(lista))+','+str(min(lista)))
