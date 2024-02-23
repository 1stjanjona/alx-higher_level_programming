#!/usr/bin/python3
'''model_state.py'''
from sqlalchemy import Column, Integer, String, MetaData, create_engine
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base, State
import sys


Base = declarative_base()


class State(Base):
    '''class of state'''
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
