##
##  Programación con Pandas
##  ===========================================================================
##
##  Construya una tabla que contenga _c0 y una lista
##  separada por ',' de los valores de la columna _c5a
##  y _c5b (unidos por ':') de la tabla tbl2.tsv
## 
##  Rta/
##      _c0                                lista
##  0     0        bbb:0,ddd:9,ggg:8,hhh:2,jjj:3
##  1     1              aaa:3,ccc:2,ddd:0,hhh:9
##  ...
##  38   38                    eee:0,fff:9,iii:2
##  39   39                    ggg:3,hhh:8,jjj:5
##
##  >>> Escriba su codigo a partir de este punto <<<
#! /usr/local/bin/python3
import numpy as np
import pandas as pd
import csv


separador=','

datos= pd.read_csv('tbl2.tsv', sep='\t', header=0 )
datos['_c5b']=datos['_c5b'].apply(str)
datos['_c5c'] = datos[['_c5a', '_c5b']].apply(lambda x: ':'.join(x), axis=1)
datos.sort_values(['_c0','_c5c'],inplace=True)
Tabla=datos[['_c0','_c5c']].groupby('_c0')['_c5c'].apply((separador.join)).reset_index()
Tabla.rename(columns={'_c5c':'lista'},inplace=True)
print(Tabla)

