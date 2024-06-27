import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    email = Column(String(250), unique=True, nullable=False)
    password = Column(String(250), nullable=False)

    # Relación con los favoritos de planetas
    favorite_planets = relationship("Favorite_planet", back_populates="user")

    # Relación con los favoritos de los personajes
    favorite_characters = relationship("Favorite_character", back_populates="user")

class Planet(Base):
    __tablename__ = "planet"
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

    # Relación con los favoritos de los planetas
    favorite_planets = relationship("Favorite_planet", back_populates="planet")
    #favorite_planet_id = Column(Integer, ForeignKey("favorite_planet.id"))

class Character(Base):
    __tablename__ = "character"
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

    # Relación con los favoritos de los personajes
    favorite_characters = relationship("Favorite_character", back_populates="character")
    #favorite_character_id = Column(Integer, ForeignKey("favorite_character.id"))

# Tablas intermediarias (los favoritos)

class Favorite_planet(Base):
    __tablename__ = "favorite_planet"
    id = Column(Integer, primary_key=True)

    # Relación con USER
    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship("User", back_populates="favorite_planets")

    # Relación con PLANET
    planet_id = Column(Integer, ForeignKey("planet.id"))
    planet = relationship("Planet", back_populates="favorite_planets")

class Favorite_character(Base):
    __tablename__ = "favorite_character"
    id = Column(Integer, primary_key=True)

    # Relación con USER
    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship("User", back_populates="favorite_characters")

    # Relación con CHARACTER
    character_id = Column(Integer, ForeignKey("character.id"))
    character = relationship("Character", back_populates="favorite_character")
    

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
