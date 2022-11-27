import pandas as pd
import numpy as np
from app.db.dbutils import Database as Database
class Student:
    _instance = None
    _dbInstance = None
    _students_df = None
    _cache = {}

    def __new__(cls):
        try:
            if cls._instance is None:
                cls._instance = super(Student, cls).__new__(cls)
            
            if cls._dbInstance is None:
                cls._dbInstance = Database()
            return cls._instance
        except:
            return None

    @classmethod
    def _updateCache(cls, key, value = True):
        cls._cache[key] = value

    @classmethod
    def _primeStudents(cls):
        cls._students_df = cls._dbInstance.ReadData(spread_sheet_name='students', filters={"student_isactive": "Y"})
        cls._updateCache('students')

    @classmethod
    def _isCached(cls, key) -> bool:
        if key in cls._cache:
            return cls._cache[key]
        else:
            return False

    @classmethod
    def ResetCache(cls):
        try:
            cls._cache = {}
        except Exception as err:
            return {"exception": err}

    @classmethod
    def GetStudents(cls) -> dict():
        try:
            if not cls._isCached('students'):
                cls._primeStudents()
            return cls._students_df.to_dict("records")
        except Exception as err:
            return {"exception": err}

    @classmethod
    def GetStudent(cls, id) -> dict():
        try:
            if not cls._isCached('students'):
                cls._primeStudents()
            return cls._students_df[cls._students_df['student_id'] == id].to_dict("records")
        except Exception as err:
            return {"exception": err}