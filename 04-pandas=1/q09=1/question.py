##
##  Programación con Pandas
##  ===========================================================================
##
##  Construya una tabla que contenga _c0 y una lista
##  separada por ',' de los valores de la columna _c4
##  del archivo `tbl1.tsv`.
##
##  Rta/
##      _c0    lista
##  0     0    b,f,g
##  1     1    a,c,f
##  ...
##  38   38      d,e
##  39   39    a,d,f
## 
##  >>> Escriba su codigo a partir de este punto <<<
import numpy as np
import pandas as pd
import csv


separador=','

datos= pd.read_csv('tbl1.tsv', sep='\t', header=0 )
#datos['_c2']=datos['_c2'].apply(str)
datos.sort_values(['_c0','_c4'],inplace=True)
Tabla=datos[['_c0','_c4']].groupby('_c0')['_c4'].apply((separador.join)).reset_index()
Tabla.rename(columns={'_c4':'lista'},inplace=True)
print(Tabla)

