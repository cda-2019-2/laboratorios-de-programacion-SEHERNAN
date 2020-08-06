##
##  Programación en Python
##  ===========================================================================
##
##  Para el archivo `data.csv`, genera una lista de tuplas que asocien las 
##  columnas 0 y 1. Cada tupla contiene un valor posible de la columna 2 y una
##  lista con todas las letras asociadas (columna 1) a dicho valor de la 
##  columna 2.
##
##  Rta/
##  ('0', ['C'])
##  ('1', ['E', 'B', 'D', 'A', 'A', 'E'])
##  ('2', ['A', 'E', 'D'])
##  ('3', ['A', 'B', 'D', 'E', 'E'])
##  ('4', ['E', 'B'])
##  ('5', ['B', 'C', 'D', 'D', 'E', 'E', 'E'])
##  ('6', ['C', 'E', 'A', 'B'])
##  ('7', ['A', 'C', 'E', 'D'])
##  ('8', ['E', 'E', 'A', 'B'])
##  ('9', ['A', 'B', 'E', 'C'])
##
##  >>> Escriba su codigo a partir de este punto <<<
f = open('data.csv', 'r')
 
tup0 = []
tup1 = []
tup2 = []
tup3 = []
tup4 = []
tup5 = []
tup6 = []
tup7 = []
tup8 = []
tup9 = []
 
 
## se itera sobre cada linea del archivo
## una a la vez
for line in f:
 
    x = line.strip()
    y = x.split()
   
    if str(y[1]) == '0':
        tup0.append(str(y[0]))
    elif str(y[1]) == '1':
        tup1.append(str(y[0]))
    elif str(y[1]) == '2':
        tup2.append(str(y[0]))
    elif str(y[1]) == '3':
        tup3.append(str(y[0]))
    elif str(y[1]) == '4':
        tup4.append(str(y[0]))
    elif str(y[1]) == '5':
        tup5.append(str(y[0]))
    elif str(y[1]) == '6':
        tup6.append(str(y[0]))
    elif str(y[1]) == '7':
        tup7.append(str(y[0]))
    elif str(y[1]) == '8':
        tup8.append(str(y[0]))
    else:
        tup9.append(str(y[0]))
f.close()
 
t0 = ('0',tup0)
t1 = ('1',tup1)
t2 = ('2',tup2)
t3 = ('3',tup3)
t4 = ('4',tup4)
t5 = ('5',tup5)
t6 = ('6',tup6)
t7 = ('7',tup7)
t8 = ('8',tup8)
t9 = ('9',tup9)
 
print(t0)
print(t1)
print(t2)
print(t3)
print(t4)
print(t5)
print(t6)
print(t7)
print(t8)
print(t9)

