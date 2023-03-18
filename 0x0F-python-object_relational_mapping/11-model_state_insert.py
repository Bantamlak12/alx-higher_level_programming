#!/usr/bin/python3
"""adds the State object “Louisiana” to the database hbtn_0e_6_usa"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == '__main__':
    """Command line arguments"""

    mysql_username = sys.argv[1]
    mysql_passwd = sys.argv[2]
    db_name = sys.argv[3]
    new_state = State(name="Louisiana")

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(mysql_username, mysql_passwd, db_name))
    Session = sessionmaker(bind=engine)
    session = Session()

    session.add(new_state)
    session.commit()
    session.close()

    state = session.query(State).filter_by(name="Louisiana").first()
    if state:
        print(state.id)
