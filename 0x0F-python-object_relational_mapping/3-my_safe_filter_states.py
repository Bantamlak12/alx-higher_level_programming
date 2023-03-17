#!/usr/bin/python3
""" displays all values in the states table of hbtn_0e_0_usa where name matches
    the argument. But this time, write one that is safe from MySQL injections!
"""
import MySQLdb
import sys

if __name__ == '__main__':
    """The code should not be executed when imported"""

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]
    state_name_searched = sys.argv[4]

    db = MySQLdb.connect(host='localhost',
                         port=3306,
                         user=mysql_username,
                         passwd=mysql_password,
                         db=db_name)
    cur = db.cursor()
    query = "SELECT * FROM states WHERE name LIKE %s ORDER BY id ASC"
    cur.execute(query, (state_name_searched + '%',))
    # a single tuple is created and is partial match

    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()
