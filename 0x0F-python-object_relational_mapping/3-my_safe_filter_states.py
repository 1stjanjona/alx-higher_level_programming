#!/usr/bin/python3
'''my safe filter states'''
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", usser=sys.argv[1].
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    match = sys.argb[4]
    cur.execute('SELECT * FROM states WHERE name LIKE %s', (match, ))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
