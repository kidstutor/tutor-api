import pandas as pd
import numpy as np
from app.entity.entity import Entity

class Student(Entity):
    _instance = None
    _df = None

    def __new__(cls):
        try:
            if cls._instance is None:
                cls._instance = super(__class__, cls).__new__(cls)
                cls._entity_identifier = {'key' : __class__.__name__,
                                          'table' : 'students'}
                cls._filters = {'student_isactive': 'Y'}
            return cls._instance
        except:
            return None

    @classmethod
    def GetStudents(cls) -> dict():
        try:
            if not cls._isCached():
                cls._primeData()
            return cls._df.to_dict("records")
        except Exception as err:
            return {"exception": err}

    @classmethod
    def GetStudent(cls, id) -> dict():
        try:
            if not cls._isCached():
                cls._primeData()
            return cls._df[cls._df['student_id'] == id].to_dict("records")
        except Exception as err:
            return {"exception": err}