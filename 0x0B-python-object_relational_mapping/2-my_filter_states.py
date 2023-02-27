#!/usr/bin/python3
"""script that takes in an argument and displays all values in the
states table of hbtn_0e_0_usa where name matches the argument"""
import MySQLdb
import sys


if __name__ == '__main__':

# Connect to MySQL database using the credentials provided as arguments
db = MySQLdb.connect(host="localhost", port=3306,
                     user=sys.argv[1], passwd=sys.argv[2],
                     db=sys.argv[3], charset="utf8")

# Create a cursor object to execute SQL queries
cursor = db.cursor()

# Use format to create the SQL query with the user input
query = "SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY id ASC"\
        .format(sys.argv[4])

# Execute the SQL query
cursor.execute(query)

# Fetch all the rows of the query result
rows = cursor.fetchall()

# Display the query results
for row in rows:
    print(row)

# Close the cursor and database connections
cursor.close()
db.close()
