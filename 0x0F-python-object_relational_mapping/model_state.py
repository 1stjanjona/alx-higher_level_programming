#!/usr/bin/python3
'''model_state.py'''
from sqlalchemy import Column, Integer, String, MetaData, create_engine
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base, State


Base = declarative_base()


class State(Base):
    '''class of state'''
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)


if __name__ == "__main__":
    engine = create_engine('mysql://username:password@localhost:3306/database')
    Base.metadata.create_all(engine)
