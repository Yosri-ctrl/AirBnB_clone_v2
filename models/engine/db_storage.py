#!/usr/bin/python3
"""____"""
import os
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.scoping import scoped_session
from sqlalchemy import create_engine
from models.base_model import BaseModel, Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class DBStorage:
    """Class DBStorage"""
    __engine = None
    __session = None
    valid_classes = ["User", "State", "City", "Amenity", "Place", "Review"]

    def __init__(self):
        """initialse"""
        self.__engine = create_engine("mysql+mysqldb://" +
                                      os.environ['HBNB_MYSQL_USER'] +
                                      ":" + os.environ['HBNB_MYSQL_PWD'] +
                                      "@" + os.environ['HBNB_MYSQL_HOST'] +
                                      ":3306/" +
                                      os.environ['HBNB_MYSQL_DB'],
                                      pool_pre_ping=True)
        try:
            if os.environ['HBNB_ENV'] == "test":
                Base.metadata.drop_all(self.__engine)
        except KeyError:
            pass

    def all(self, cls=None):
        """all"""
        storage = {}
        if cls is None:
            for cls_name in self.valid_classes:
                for instance in self.__session.query(eval(cls_name)):
                    storage[instance.id] = instance
        else:
            if cls not in self.valid_classes:
                return
            for instance in self.__session.query(eval(cls)):
                storage[instance.id] = instance

        return storage

    def new(self, obj):
        """new"""
        self.__session.add(obj)

    def save(self):
        """save"""
        self.__session.commit()

    def update(self, cls, obj_id, key, new_value):
        """update"""
        res = self.__session.query(eval(cls)).filter(eval(cls).id == obj_id)

        if res.count() == 0:
            return 0

        res.update({key: (new_value)})
        return 1

    def reload(self):
        """reload"""
        Base.metadata.create_all(self.__engine)
        file_session = sessionmaker(bind=self.__engine)
        self.__session = scoped_session(file_session)

    def delete(self, obj=None):
        """delete"""
        if obj is None:
            self.__session.delete(obj)
