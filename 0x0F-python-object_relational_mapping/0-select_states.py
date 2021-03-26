#!/usr/bin/python3
'''
An easy query to warm up.
'''

if __name__ == "__main__":
    from sys import argv
    import MySQLdb
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
