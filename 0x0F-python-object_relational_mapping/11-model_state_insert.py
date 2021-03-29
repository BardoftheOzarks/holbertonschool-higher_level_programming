#!/usr/bin/python3
'''
Adds State obj "Louisiana" to input database
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

    row = State(name='Louisiana')
    Session.add(row)
    Session.commit()
    print(row.id)
    Session.close()
