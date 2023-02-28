#!/usr/bin/python3
"""Script that prints the State object with the name passed as argument
from the database hbtn_0e_6_usa"""
import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    # Database connection
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                        .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                        pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the database for the state name
    state = session.query(State).filter(State.name == sys.argv[4]).first()

    # Print the state id or "Not found" if the state was not found
    if state is not None:
        print(state.id)
    else:
        print("Not found")

    # Close the session
    session.close()
