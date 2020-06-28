#!/usr/bin/python3
"""
Base class for models contains id, created_at
and updated at attributes.
"""
import uuid
from datetime import datetime
import models


class BaseModel():
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at':
                    value = datetime.strptime(
                        value, "%Y-%m-%dT%H:%M:%S.%f")
                if key == 'updated_at':
                    value = datetime.strptime(
                        value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

        def __str__(self):
            return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.now()


	def save(self):
		self.updated_at = datetime.now()
		models.storage.save()

	def to_dict(self):
		dic = self.__dict__
		dic['__class__'] = type(self).__name__
		dic['created_at'] = self.created_at.isoformat()
		dic['updated_at'] = self.updated_at.isoformat()
		return dic

