#!/usr/bin/python3
"""script that lists all states with a name
starting with N from the database hbtn_0e_0_usa"""
import MySQLdb
import sys


if __name__ == '__main__':
    # connect to the database
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], charset="utf8")
    # create a cursor object
    cr = db.cursor()
    # execute the SQL query to retrieve all states starting with "N"
    query = " ".join([
        "SELECT * FROM states",
        "WHERE name LIKE BINARY 'N%'",
        "ORDER BY id ASC"])
    cr.execute(query)
    # fetch all rows and print them
    rows = cr.fetchall()
    for row in rows:
        print(row)
    cr.close()
    # close the database connection
    db.close()
