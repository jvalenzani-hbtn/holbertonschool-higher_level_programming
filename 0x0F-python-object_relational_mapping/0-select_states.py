#!/usr/bin/python3
"""Aca haciendo una consulta a la BD con la barra."""

from sys import argv
import MySQLdb
"""Aca haciendo una consulta a la BD con la barra."""

MY_HOST = "localhost"
MY_USER = argv[1]
MY_PASS = argv[2]
MY_DB = argv[3]
# Hago la conexion a la BD. Obtengo un objeto db
try:
    db = MySQLdb.connect(host=MY_HOST, user=MY_USER, passwd=MY_PASS, db=MY_DB)
    # Obtengo un cursor para ejecutar las consultas
    cur = db.cursor()
    # Ejecuto consulta usando el cursor
    cur.execute("SELECT * FROM states ORDER BY id")
    # Obtengo todas las filas
    rows = cur.fetchall()
    # Recorro el resultado
    for r in rows:
        print(r)
    db.close()
except Exception as e:
    print("ERROR: {}".format(e))

if __name__ == 'main':
    pass
