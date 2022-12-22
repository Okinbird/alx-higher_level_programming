#!/usr/bin/python3
"""
    Displays all cities of a given state from the
    states table of the database hbtn_0e_4_usa.
    Safe from SQL injections.
    Usage: ./5-filter_cities.py <mysql username> \
                                <mysql password> \
                                <database name> \
                                <state name searched>
"""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    cursor = db.cursor()
    cursor.execute("""SELECT cities.name FROM
                cities INNER JOIN states ON states.id=cities.state_id
                WHERE states.name=%s""", (sys.argv[4],))
    rows = cursor.fetchall()
    tmp = list(row[0] for row in rows)
    print(*tmp, sep=", ")
    cursor.close()
    db.close()
