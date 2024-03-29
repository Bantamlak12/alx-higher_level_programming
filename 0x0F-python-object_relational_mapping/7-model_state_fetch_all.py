#!/usr/bin/python3
""" lists all State objects from the database hbtn_0e_6_usa"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == '__main__':
    """Command line arguments"""

    mysql_username = sys.argv[1]
    mysql_passwd = sys.argv[2]
    db_name = sys.argv[3]

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(mysql_username, mysql_passwd, db_name))

    # create a session factory
    Session = sessionmaker(bind=engine)

    # create a session
    session = Session()

    # quering the session
    states = session.query(State).all()

    for state in states:
        print('{}: {}'.format(state.id, state.name))
