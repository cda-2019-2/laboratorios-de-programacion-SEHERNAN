##
##  Programación en Bash
##  ===========================================================================
##
##  Usando los archivos `data1.csv`, `data2.csv`, `data3.csv`, escriba en el
##  archivo `script.sh`  un programa en Bash que imprima en pantalla
##  la siguiente salida por linea:
## 
##  * El nombre del archivo.
##  * El número de la línea procesada.
##  * La letra de la primera columna del archivo.
##  * La cadena de tres letras y el valor asociado de la columna 2 del archivo original. 
##
##  Note que se genera una línea de salida por cada cadena de tres letras.
##   
##  Rta/
##
##  data1.csv,1,E,jjj:3
##  data1.csv,1,E,bbb:0
##  ...
##  data3.csv,3,B,hhh:1
##  data3.csv,3,B,ddd:2
##
##  >>> Escriba su codigo a partir de este punto <<<
for file in *.csv;do sed '/^.$/d' $file > "$(basename "$file" .csv).1.csv"; done      #Elimina filas vacías
for file in *.1.csv; do awk '{print NR "," $s}' $file > "$(basename "$file" .csv).2.csv"; done       #Coloca el número de cada línea
for file in *.2.csv;do sed "s/^/"${file}\,"/" $file > "$(basename "$file" .csv).3.csv";done      #Coloca el nombre del archivo en cada fila
for file in *.3.csv;do sed 's/[[:space:]]//g' $file > "$(basename "$file" .csv).4.csv";done    #Elimina tabulador
for file in *.4.csv;do sed 's/\([A-Z]\)/\1,/g' $file > "$(basename "$file" .csv).5.csv";done    #Agregar coma después de la mayúscula
awk -F',' '{ for(i=4;i<=NF;i++) print $1,$2,$3,$i}' OFS=',' *.5.csv > data_final.csv    #Para dividir la cuarta columna  en varias líneas hasta que encuentre la coma
sed -e 's/.1.2//g' data_final.csv > Resultado.1    #Para reemplazar los .1.2 por nada
rm {.1.csv,.2.csv,.3.csv,.4.csv,*.5.csv,data_final.csv}        #Elimina los archivos sobrantes
cat Resultado.1    #Muestra la solución
rm Resultado.1
