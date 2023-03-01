#!/usr/bin/python3
"""Script that prints all City objects from the database hbtn_0e_14_usa"""
import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    # Creates an engine instance with the provided credentials
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    # Creates all the tables in the database (in this case, State and City)
    Base.metadata.create_all(engine)
    # Creates a session to connect to the database
    Session = sessionmaker(bind=engine)
    session = Session()
    # Queries all State and City objects that have the same state_id,
    # and orders by City id
    res = session.query(State, City).filter(State.id == City.state_id) \
                                    .order_by(City.id).all()
    # Prints out the name of each state and the corresponding city name and id
    for state, city in res:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    # Closes the session
    session.close()
