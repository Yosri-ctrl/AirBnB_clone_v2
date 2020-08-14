#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import models
from os import getenv


class State(BaseModel, Base):
    """ State class """
    name = Column(String(128), nullable=False)
    __tablename__ = "states"

    cities = relationship("City", backref="state",
                          cascade="all, delete")

    if getenv('HBNB_TYPE_STORAGE', '') != 'db':
        @property
        def cities(self):
            """___"""
            all_cities = models.storage.all("City")
            list = []
            for i in all_cities:
                if all_cities[i].state_id == self.id:
                    list.append(all_cities[i])
            return list
