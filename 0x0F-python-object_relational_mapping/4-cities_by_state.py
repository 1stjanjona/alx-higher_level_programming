#!/usr/bin/python3
'''my filter states'''
import MySQLdb
import sys


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".
            format(sys.argv[0]))
        sys.exit(1)
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]
    try:
        db = MySQLdb.connect(host="localhost", user=username,
                             passwd=password, db=database, port=3306)
        cur = db.cursor()
        query = "SELECT * FROM cities ORDER BY id;"
        cur.execute(query)
        rows = cur.fetchall()
        for row in rows:
            print(row)
    except MySQLdb.Error as e:
        print("MySQL Error {}: {}".format(e.args[0], e.args[1]))
        sys.exit(1)
    finally:
        if db:
            cur.close()
            db.close()
