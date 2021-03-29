#!/usr/bin/python3
'''
Lists all City objects within a state in a database
'''
if __name__ == '__main__':
    from sys import argv
    from model_state import Base, State
    from model_city import City
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = sessionmaker(bind=engine)
    Session = session()
    for instance in Session.query(City, State).join(
            State, City.state_id == State.id).order_by(City.id.asc()).all():
        print("{}: ({}) {}".format(instance[1].name, instance[0].id,
                                   instance[0].name))
    Session.close()
