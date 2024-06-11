#!/usr/bin/python3

"""
    lists all cities from the database hbtn_0e_4_usa
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )
    c = db.cursor()

    # SQL codes here
    c.execute("SELECT cities.id, cities.name, states.name FROM cities\
              JOIN states ON cities.state_id = states.id\
              ORDER BY cities.id ASC")
    [print(x) for x in c.fetchall()]
