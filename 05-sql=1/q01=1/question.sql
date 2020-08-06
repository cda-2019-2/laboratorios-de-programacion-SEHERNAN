--
--  Programacion basica en SQL
--  ===========================================================================
-- 
--  La tabla `data` tiene la siguiente estructura:
-- 
--    K0  CHAR(1)
--    K1  INT
--    c12 FLOAT
--    c13 INT
--    c14 DATE
--    c15 FLOAT
--    c16 CHAR(4)
--
--  Escriba una consulta en SQL que devuelva la suma del campo c12.
-- 
--  Rta/
--     SUM(c12)
--  0  15137.63
--
--  >>> Escriba su codigo a partir de este punto <<<
import sqlite3
conn = sqlite3.connect('data.db')
cur = conn.cursor()

conn.executescrip("""
DROP TABLE IF EXISTS data;

CREATE TABLE data (
    K0  CHAR(1),   
    K1  INT,        
    c12 FLOAT,
    c13 INT,
    c14 DATE,
    c15 FLOAT,
    c16 CHAR(4));

""")
conn.commit()

with open ('data.csv','rt') as f:
    data = f.readlines()

data [line[:-1]if line[-1] == '\n' else line for line in data]

data = [line.split(',') for line in data]

data = [tuble(line) for line in data]

cur.executemany(INSERT INTO data VALUES (?,?,?,?,?,?,?), data)

cur.execute ("SELECT SUM(C12) FROM data;").fetchall()






