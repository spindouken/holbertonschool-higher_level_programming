#!/usr/bin/python3
"""Script that lists all State objects that contain the letter 'a'
from the database hbtn_0e_6_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Create an engine to connect to the database using the command line arguments
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                        .format(sys.argv[1], sys.argv[2],
                                sys.argv[3]), pool_pre_ping=True)
    # Create the table if it doesn't exist
    Base.metadata.create_all(engine)
    # Create a session to query the database
    Session = sessionmaker(bind=engine)
    session = Session()
    # Query all states containing 'a' and order by id
    states_with_a = session.query(State).filter(State.name.like('%a%')).order_by(State.id)

    # Print out the states that contain 'a'
    for state in states_with_a:
        print(f"{state.id}: {state.name}")

    session.close()
