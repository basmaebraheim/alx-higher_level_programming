#!/usr/bin/python3
"""
Contains city class
"""
from model_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey

class City(Base):
    """
    Class defines each city
    """
    __tablename__ = 'cities'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
