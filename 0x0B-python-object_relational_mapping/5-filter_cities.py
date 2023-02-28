#!/usr/bin/python3

"""
This script takes in the name of a state as an argument and
lists all cities of that state, using hbtn_0e_4_usa.
"""

import MySQLdb
import sys

# Check if this script is being run directly and not being imported
if __name__ == '__main__':
    
    # Connect to the database using given credentials
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        charset="utf8"
    )
    
    # Create a cursor object to execute SQL queries
    cursor = db.cursor()

    # Build the SQL query
    query = " ".join([
        "SELECT cities.name FROM cities",
        "INNER JOIN states ON states.id = cities.state_id",
        "WHERE states.name LIKE BINARY '{}'",
        "ORDER BY cities.id",
    ]).format(sys.argv[4])

    # Execute the query
    cursor.execute(query)

    # Fetch all results
    results = cursor.fetchall()

    # Join the results into a comma-separated string
    results_str = ', '.join([i[0] for i in results])

    # Print the results string
    print(results_str)

    # Close the cursor and database connection
    cursor.close()
    db.close()
