#!/usr/bin/python3
"""BaseModel module: Defines all common"""

import uuid
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime

Base = declarative_base()


class BaseModel:
    """Defines all common attributes/methods for other classes."""
    id = Column(String(60), primary_key=True, default=lambda: uuid.uuid4().hex)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(
        DateTime, default=datetime.utcnow, 
        nullable=False, onupdate=datetime.utcnow)

    def __init__(self, *args, **kwargs):
        """Initializes a new instance of BaseModel."""
        from models import storage
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ('created_at', 'updated_at'):
                        value = datetime.fromisoformat(value)
                    setattr(self, key, value)
            storage.new(self)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """String representation of the BaseModel class."""
        return "[{}] ({}) {}".format(
                self.__class__.__name__,
                self.id,
                self.__dict__
            )

    def __repr__(self):
        """
        returns string repr
        """
        return (self.__str__())

    def save(self):
        """Updates 'updated_at' with the current datetime."""
        self.updated_at = datetime.now()
        from models import storage
        storage.save()

    def delete(self):
        from models import storage
        storage.delete(self)

    def to_dict(self):
        """Returns a dictionary containing all keys/values."""
        my_dict = {
            key: value.isoformat()
            if isinstance(value, datetime)
            else value for key, value in self.__dict__.items()
        }
        my_dict['__class__'] = self.__class__.__name__
        return my_dict
