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

    for state in Session.query(State).all():
        if 'a' in state.name:
            Session.delete(state)
    Session.commit()
    Session.close()
