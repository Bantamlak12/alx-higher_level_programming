#!/usr/bin/python3
""" prints the State object with the name passed as
    argument from the database hbtn_0e_6_usa.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == '__main__':
    """Command line arguments"""

    mysql_username = sys.argv[1]
    mysql_passwd = sys.argv[2]
    db_name = sys.argv[3]
    state_name_to_search = sys.argv[4]

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(mysql_username, mysql_passwd, db_name))
    Session = sessionmaker(bind=engine)
    session = Session()

    # .first() method is used to retrieve only the first result of the query
    state = session.query(State).filter_by(name=state_name_to_search).first()

    if state:
        print(state.id)
    else:
        print('Not found')
