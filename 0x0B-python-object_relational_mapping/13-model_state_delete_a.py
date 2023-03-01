#!/usr/bin/python3
"""
Script that deletes all State objects with a name
containing letter 'a' from the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # create an engine for our MySQL database with the given user credentials
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # create all tables in the engine's metadata
    Base.metadata.create_all(engine)

    # create a session factory bound to the engine
    Session = sessionmaker(bind=engine)

    # create a session instance
    session = Session()

    # query all State objects with names containing letter 'a', and delete them
    # (with option to synchronize the session with the database)
    result = session.query(State).filter(State.name.like('%a%')) \
                    .delete(synchronize_session='fetch')

    # commit the transaction
    session.commit()

    # close the session
    session.close()
