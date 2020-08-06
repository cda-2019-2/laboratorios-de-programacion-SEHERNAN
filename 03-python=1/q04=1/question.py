##
##  Programación en Python
##  ===========================================================================
##
##  La columna 3 del archivo `data.csv` contiene una fecha en formato 
##  `YYYY-MM-DD`. Imprima la cantidad de registros por cada mes separados
##  por comas, tal como se muestra a continuación.
##
##  Rta/
##  01,3
##  02,4
##  03,2
##  04,4
##  05,3
##  06,3
##  07,5
##  08,6
##  09,3
##  10,2
##  11,2
##  12,3
##
##  >>> Escriba su codigo a partir de este punto <<<
archivo = open('data.csv','r').readlines()
 
archivo1 = [z.replace('\n', '') for z in archivo]
archivo2 = [z.replace('\t', '-') for z in archivo1]
archivo3 = [z.split(',') for z in archivo2]
archivo4 = [z[0] for z in archivo3[0:]]
archivo5 = [z[8:12].split('-') for z in archivo4[0:]]
archivo6 = [z[1].split('-') for z in archivo5[0:]]
archivo7 = [z[0] for z in archivo6[0:]]
print('01,'+str(archivo7.count('01')))
print('02,'+str(archivo7.count('02')))
print('03,'+str(archivo7.count('03')))
print('04,'+str(archivo7.count('04')))
print('05,'+str(archivo7.count('05')))
print('06,'+str(archivo7.count('06')))
print('07,'+str(archivo7.count('07')))
print('08,'+str(archivo7.count('08')))
print('09,'+str(archivo7.count('09')))
print('10,'+str(archivo7.count('10')))
print('11,'+str(archivo7.count('11')))
print('12,'+str(archivo7.count('12')))
