#!/usr/bin/python3
"""lists all cities from the database hbtn_0e_4_usa"""

import MySQLdb
import sys

if __name__ == '__main__':
    mysql_username = sys.argv[1]
    mysql_passwd = sys.argv[2]
    db_name = sys.argv[3]

    db = MySQLdb.connect(host='localhost',
                         port=3306,
                         user=mysql_username,
                         passwd=mysql_passwd,
                         db=db_name)
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name \
                 FROM cities, states WHERE cities.state_id = states.id")

    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()
