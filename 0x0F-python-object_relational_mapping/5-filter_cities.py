#!/usr/bin/python3
'''my filter states'''
import MySQLdb
import sys


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <state_name>".
            format(sys.argv[0]))
        sys.exit(1)
    username, password, database, state_name = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
    try:
        db = MySQLdb.connect(host="localhost", user=username,
                             passwd=password, db=database, port=3306)
        cur = db.cursor()
        query = "SELECT cities.name FROM cities JOIN states ON cities.state_id = states.id WHERE states.name = %s ORDER BY cities.id;"
        cur.execute(query, (state_name,))
        rows = cur.fetchall()
        city_names = [row[0] for row in rows]
        result = ", ".join(city_names)
        print(result)
    except MySQLdb.Error as e:
        print("MySQL Error {}: {}".format(e.args[0], e.args[1]))
        sys.exit(1)
    finally:
        if db:
            cur.close()
            db.close()
