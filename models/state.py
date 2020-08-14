#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import models


class State(BaseModel, Base):
    """ State class """
    name = Column(String(128), nullable=False)
    __tablename__ = "states"

    cities = relationship("City", backref="state",
                          cascade="all, delete")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @property
    def cities(self):
        all_cities = models.storage.all("City")
        list = []
        for c_id in all_cities:
            if all_cities[c_id].state_id == self.id:
                list.append(all_cities[c_id])

        return list
