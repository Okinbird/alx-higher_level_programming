#!/usr/bin/python3
"""
    Lists all states from the database hbtn_0e_0_usa.
    Usage: ./0-select_states.py <mysql username> \
                                <mysql password> \
                                <database name>
"""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT * FROM `states`")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()
