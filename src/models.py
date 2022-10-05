import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base ()
class User(Base):
    __tablename__ = 'users'
    id = Column (Integer, primary_key = True)
    firstname = Column (String(30), nullable=False) 
    lastname = Column (String(30), nullable=False) 
    email = Column (String(50), nullable=False) 
    password = Column (String(10), nullable=False) 

class Favorite (Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    users_id = Column(Integer, ForeignKey('users.id'))
    characters_id = Column(Integer, ForeignKey('characters.id'))
    planets_id = Column(Integer, ForeignKey('planets.id'))
    user = relationship('User')

class Planet(Base):
    __tablename__ = 'planets'

    id = Column(Integer, primary_key = True)
    name = Column (String(30), nullable=False)
    climate = Column (String(50), nullable=False) 
    diameter = Column (String(50), nullable=False) 
    films = Column (String(50), nullable=False) 
    gravity = Column (String(50), nullable=False) 
    population = Column (String(50), nullable=False) 
    residents = Column (String(50), nullable=False) 
    terrain = Column (String(50), nullable=False) 

class Character(Base):
    __tablename__ = 'characters'
    
    id = Column(Integer, primary_key = True)
    films = Column (String(50), nullable=False) 
    name = Column (String(30), nullable=False) 
    species = Column (String(50), nullable=False) 
    starships = Column (String(50), nullable=False) 
    role_by = Column (String(50), nullable=False) 

render_er(Base, 'diagram.png')