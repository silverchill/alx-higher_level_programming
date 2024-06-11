#!/usr/bin/python3

"""
    takes in the name of a state as an
    argument and lists all cities of that state
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
    query = "SELECT cities.name FROM cities\
        JOIN states ON cities.state_id = states.id\
        WHERE states.name = %s"
    c.execute(query, (argv[4],))
    j = []
    [j.append(*x) for x in c.fetchall()]
    print(*j, sep=', ')

    c.close()
    db.close()
