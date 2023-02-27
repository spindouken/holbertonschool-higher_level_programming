#!/usr/bin/python3
"""script that lists all states from the database hbtn_0e_0_usa"""
import MySQLdb
import sys


if __name__ == '__main__':
    # connect to the database
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], charset="utf8")
    # create a cursor object using cursor() method
    cursor = db.cursor()
    # execute the SQL query to retrieve all states
    cursor.execute("SELECT * FROM states ORDER BY states.id")
    # fetch all rows and print them out
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    # close cursor buffer
    cursor.close()
    # close the database connection
    db.close()
