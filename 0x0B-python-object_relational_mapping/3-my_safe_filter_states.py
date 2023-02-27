#!/usr/bin/python3
"""script that takes in an argument and displays all values in the
states table of hbtn_0e_0_usa where name matches the argument
and it is safe from MySQL injections"""
import MySQLdb
import sys


if __name__ == "__main__":
    # Connect to the database
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], charset="utf8")

    # Create a cursor object
    cursor = db.cursor()

    # Sanitize the input provided by the user
    state_name = MySQLdb.escape_string(sys.argv[4])

    # Build the SQL query using parameterized queries
    query = """
            SELECT * FROM states
            WHERE name = %s
            ORDER BY id ASC
            """

    # Execute the SQL query using the sanitized input
    cursor.execute(query, (state_name,))

    # Fetch all the rows and store them in a variable
    rows = cursor.fetchall()

    # Display the rows
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cursor.close()
    db.close()
