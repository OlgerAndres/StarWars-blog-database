import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String,Float ,Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

# class Person(Base):
#     __tablename__ = 'person'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)

# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

class Personajes(Base):
    __tablename__ = 'personajes'
    id = Column(Integer,primary_key=True)
    name = Column(String(25))
    heigth = Column(Integer)
    mass = Column(Integer)
    hair_color = Column(String(25))
    skin_color = Column(String(25))
    eye_color = Column(String(25))
    birth_year = Column(String(25))
    gender = Column(String(40))
    url = Column(String(100))

class Planetas(Base):
    __tablename__ = 'planetas'
    id = Column(Integer,primary_key=True)
    name = Column(String(40))
    rotation_period = Column(Integer)
    orbital_period = Column(Integer)
    diameter = Column(Integer)
    climate = Column(String(40))
    gravity = Column(String(40))
    terrain = Column(String(40))
    surface_water = Column(Integer)
    population = Column(Integer)

class Usuarios(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer,primary_key=True)
    name = Column(String(40))
    correo = Column(String(100))
    contrasena = Column(String(100))
    
class Favoritos(Base):
    __tablename__ = 'favoritos'
    id = Column(Integer,primary_key=True)
    usuarios_id = Column(Integer,ForeignKey('usuarios.id'))
    planetas_id = Column(Integer,ForeignKey('planetas.id'))
    personajes_id = Column(Integer,ForeignKey('personajes.id'))
    
    
    
    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')