#!/usr/bin/python3
'''
List first State object in a database
'''
if __name__ == '__main__':
    from sys import argv
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = sessionmaker(bind=engine)
    Session = session()
    state = Session.query(State).order_by(State.id.asc()).first()
    if state is None:
        print('Nothing')
    else:
        print("{}: {}".format(state.id, state.name))

    Session.close()
