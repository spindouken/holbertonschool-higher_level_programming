#!/usr/bin/python3
"""script that lists all cities from the database hbtn_0e_4_usa"""
import MySQLdb
import sys


if __name__ == '__main__':

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], charset="utf8")
    # create a cursor
    cursor = db.cursor()
    query = " ".join([
        "SELECT cities.id, cities.name, states.name FROM cities",
        "INNER JOIN states ON states.id = cities.state_id",
        "ORDER BY cities.id"
        ])
    cursor.execute(query)

    # fetch all the rows as a list of tuples
    rows = cursor.fetchall()

    # print the rows
    for row in rows:
        print(row)

    # close the cursor and database connection
    cursor.close()
    db.close()
