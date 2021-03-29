#!/usr/bin/python3
'''
Lists all State objects in a database
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
    states = []
    for state in Session.query(State).order_by(State.id.asc()).all():
        if argv[4] in state.name:
            states.append(state)
    if len(states) == 0:
        print('Not found')
    else:
        for state in states:
            print("{}".format(state.id))
    Session.close()
