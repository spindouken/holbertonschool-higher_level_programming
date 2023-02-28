#!/usr/bin/python3
"""script that prints the first State object from the database hbtn_0e_6_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == '__main__':
    # Create a connection to the database using SQLAlchemy
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the first state and print its representation
    query = session.query(State).order_by(State.id).first()
    if query is None:
        print("Nothing")
    else:
        print("{}: {}".format(query.id, query.name))

    # Close the session
    session.close()
