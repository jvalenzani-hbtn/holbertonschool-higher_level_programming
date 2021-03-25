#!/usr/bin/python3
'''
Aca haciendo una consulta a la BD con la barra.
'''

from sys import argv
import MySQLdb

if __name__ == 'main':
  MY_HOST = "localhost"
  MY_USER = argv[1]
  MY_PASS = argv[2]
  MY_DB = argv[3]
  try:
      db = MySQLdb.connect(host=MY_HOST, user=MY_USER, passwd=MY_PASS, db=MY_DB)
      cur = db.cursor()
      cur.execute("SELECT * FROM states ORDER BY id")
      rows = cur.fetchall()
      for r in rows:
          print(r)
      db.close()
  except Exception as e:
      print("ERROR: {}".format(e))
