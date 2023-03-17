#!/usr/bin/python3
""" A module that  takes in an argument and displays all values
    in the states table of hbtn_0e_0_usa where name matches the argument
"""
import MySQLdb
import sys

if __name__ == '__main__':
    """The code should not be executed when imported"""

    mysql_username = sys.argv[1]
    mysql_passwd = sys.argv[2]
    db_name = sys.argv[3]
    state_name_searched = sys.argv[4]

    db = MySQLdb.connect(host='localhost',
                         port=3306,
                         user=mysql_username,
                         passwd=mysql_passwd,
                         db=db_name)

    cur = db.cursor()

    cur.execute("SELECT * FROM states WHERE name LIKE '{}%' \
                 ORDER by id ASC".format(state_name_searched))

    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()
