#!/usr/bin/python3
"""
    Displays all values in the states table of the database hbtn_0e_0_usa
    whose name matches that supplied as argument.
    Safe from SQL injections.
    Usage: ./3-my_safe_filter_states.py <mysql username> \
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
    match = sys.argv[4]
    cursor.execute("SELECT * FROM states WHERE name LIKE %s", (match, ))
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()
    
