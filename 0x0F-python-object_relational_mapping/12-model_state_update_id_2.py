#!/usr/bin/python3
"""
    Changes the name of the State object with id = 2 to
    New Mexico in the database hbtn_0e_6_usa.
    Usage: ./12-model_state_update_id_2.py <mysql username> /
                                           <mysql password> /
                                           <database name>
"""

import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    new_instance = session.query(State).filter_by(id=2).first()
    new_instance.name = 'New Mexico'
    session.commit()
    session.close()
