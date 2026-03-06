#!/usr/bin/python3
"""
Prints the first State object from the database hbtn_0e_6_usa
using SQLAlchemy
"""


import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            sys.argv[1],
            sys.argv[2],
            sys.argv[3]
            ),
        pool_pre_ping=True
        )
    session = Session(engine)
    state = session.query(State).order_by(State.id).first()
    if state:
        print("{}: {}".format(state.id, state.name))
    else:
        print("Nothing")

    session.close()
