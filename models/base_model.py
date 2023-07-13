#!/usr/bin/python3
"""State BaseMode Class for AirBnB Project."""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Basemodel for AirBnB Project"""

    def __init__(self, *args, **kwargs):
        """Initialize BaseModel"""

        tformat = "%Y-%m-%dT%H:%M%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for key, val in kwargs.items():
                if key == "created_at" or key == "update_at":
                    self.__dict__[key] = datetime.strptime(val, tformat)
                else:
                    self.__dict__[key] = val
            else:
                models.storage.new(self)
    
    def __str__(self):
        """Return str representation of BaseModel"""

        clsName = self.__class__.__name__
        return "[{}] ({}) {}".format(clsName, self.id, self.__dict__)


    def save(self):
        """Func to update public instance attribute"""
        
        self.update_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """Return the dict of BaseModel"""

        b_dict = self.__dict__.copy()
        b_dict["created_at"] = self.created_at.isoformat()
        b_dict["updated_at"] = self.updated_at.isoformat()
        b_dict["__class__"] = self.__class__.__name__
        return b_dict
