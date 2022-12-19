#!/usr/bin/python3
""" 
    Lists all states with a name starting with N from the database hbtn_0e_0_usa.
    Usage: ./1-filter_states.py <mysql username> \
                                <mysql password> \
                                <database name>
"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    cursor = db.cursor()
    cursor.execute("""SELECT * FROM states WHERE name
                   LIKE BINARY 'N%' ORDER BY states.id""")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()
