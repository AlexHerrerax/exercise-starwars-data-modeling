import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'User'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)

class Planet(Base):
    __tablename__ = 'Planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    diameter= Column(String(250), nullable=False)
    population = Column(String(250), nullable=False)
    climate =Column(String(250), nullable=False)

class People(Base):
    __tablename__ ='People'
    id = Column(Integer, primary_key=True)
    name =Column(String(250), nullable=False)
    gender=Column(String(250), nullable=False)
    height =Column(String(250), nullable=False)
    mass =Column(String(250), nullable=False)

class F_Planet(Base):
    __tablename__ ='favorite_planet'
    id=Column(Integer, primary_key=True)
    user_id=Column(Integer, ForeignKey(User.id) )
    planet_id=Column(Integer, ForeignKey(Planet.id) )

class F_People(Base):
    __tablename__ ='favorite_people'
    id = Column(Integer, primary_key=True)
    user_id= Column(Integer, ForeignKey(User.id) )
    people_id= Column(Integer, ForeignKey(People.id) )


    

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')