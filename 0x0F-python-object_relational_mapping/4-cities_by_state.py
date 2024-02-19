#!/usr/bin/python3
'''4-cities_by_state.py'''
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', user=sys.argv[1],
                         passwd=sys.argv[2], sb=sys.argv[3], port=3306)
    cur = db.cursor()
    cur.execute('''SELECT cities.id, cities.name, states.name FROM
                cities INNER JOIN states ON states.id=cities.state_id''')
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
