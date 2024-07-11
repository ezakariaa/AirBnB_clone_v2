#!/usr/bin/python3
"""
Creates a unique FileStorage instance.
"""

from os import getenv
from .base_model import BaseModel, Base
from .engine.db_storage import DBStorage

if getenv('HBNB_TYPE_STORAGE') == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

storage.reload()
