#!/usr/bin/python3
"""
    Lists all City objects from the database hbtn_0e_101_usa.
    Usage: ./102-relationship_cities_states_list.py <mysql username> /
                                                    <mysql password> /
                                                    <database name>
"""

import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for instance in session.query(State).order_by(State.id):
        for city_ins in instance.cities:
            print(city_ins.id, city_ins.name, sep=": ", end="")
            print(" -> " + instance.name)
    session.close()
