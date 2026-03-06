#!/usr/bin/python3
"""
Deletes all State objects with a name containing the letter 'a'
from the database, using SQLAlchemy.
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

    states_list = (
        session.query(State)
        .filter(State.name.contains("a"))
        .all()
    )

    for state in states_list:
        session.delete(state)
    session.commit()

    session.close()
