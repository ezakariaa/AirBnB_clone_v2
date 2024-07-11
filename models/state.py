#!/usr/bin/python3
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column,  String
import models
import shlex


class State(BaseModel, Base):
    """State Class"""
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade='all, delete, delete-orphan',
                          backref="state")

    @property
    def cities(self):
        """Retourne la liste des villes associées à cet état"""
        cities_list = []
        for city in models.storage.all(City).values():
            if city.state_id == self.id:
                cities_list.append(city)
        return cities_list
