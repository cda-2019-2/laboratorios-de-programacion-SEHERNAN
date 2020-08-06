##
##  Programación en Python
##  ===========================================================================
##
##  Genere una lista de tuplas, donde cada tupla contiene en la primera 
##  posicion, el valor de la segunda columna; la segunda parte de la 
##  tupla es una lista con las letras (ordenadas y sin repetir letra) 
##  de la primera  columna que aparecen asociadas a dicho valor de la 
##  segunda columna. Esto es:
##
##  Rta/
##  ('0', ['C'])
##  ('1', ['A', 'B', 'D', 'E'])
##  ('2', ['A', 'D', 'E'])
##  ('3', ['A', 'B', 'D', 'E'])
##  ('4', ['B', 'E'])
##  ('5', ['B', 'C', 'D', 'E'])
##  ('6', ['A', 'B', 'C', 'E'])
##  ('7', ['A', 'C', 'D', 'E'])
##  ('8', ['A', 'B', 'E'])
##  ('9', ['A', 'B', 'C', 'E'])
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
 
def unique(list1): 
 
  
    # intilize a null list 
    unique_list = [] 
      
    # traverse for all elements 
    for x in list1: 
        # check if exists in unique_list or not 
        if x not in unique_list: 
            unique_list.append(x) 
    return unique_list
 
tup0 = unique(tup0)
tup1 = unique(tup1)
tup2 = unique(tup2)
tup3 = unique(tup3)
tup4 = unique(tup4)
tup5 = unique(tup5)
tup6 = unique(tup6)
tup7 = unique(tup7)
tup8 = unique(tup8)
tup9 = unique(tup9)
 
t0 = ('0',sorted(tup0))
t1 = ('1', sorted(tup1))
t2 = ('2',sorted(tup2))
t3 = ('3',sorted(tup3))
t4 = ('4',sorted(tup4))
t5 = ('5',sorted(tup5))
t6 = ('6',sorted(tup6))
t7 = ('7',sorted(tup7))
t8 = ('8',sorted(tup8))
t9 = ('9',sorted(tup9))
 
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

