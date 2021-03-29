#!/usr/bin/python3
'''
Class definition of City
'''
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base, State


class City(Base):
    '''class to link to table "cities"'''
    __tablename__ = 'cities'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
