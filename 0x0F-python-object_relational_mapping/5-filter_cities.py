#!/usr/bin/python3
'''
The right way, or the highway. Use the power of your DBMS to keep your code clean. :)
'''

if __name__ == "__main__":
    from sys import argv
    import MySQLdb
    MY_HOST = "localhost"
    MY_USER = argv[1]
    MY_PASS = argv[2]
    MY_DB = argv[3]
    STATE_NAME = argv[4]
    try:
        db = MySQLdb.connect(host=MY_HOST, user=MY_USER, passwd=MY_PASS, db=MY_DB)
        cur = db.cursor()
        cur.execute("SELECT GROUP_CONCAT(c.name SEPARATOR ', ') FROM states s, cities c where s.id = c.state_id and s.name = %s order by c.id", (STATE_NAME,))
        print(cur.fetchone()[0])
        db.close()
    except Exception as e:
        print("ERROR: {}".format(e))
