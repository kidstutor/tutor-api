import pandas as pd
import numpy as np
from app.db.dbutils import Database as Database
class Student:
    _instance = None
    _dbInstance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Student, cls).__new__(cls)
        
        if cls._dbInstance is None:
            cls._dbInstance = Database()
        return cls._instance

    @classmethod
    def GetStudents(cls) -> dict():
        try:
            students_df =  cls._dbInstance.ReadData(spread_sheet_name='students')
            return students_df.to_dict("records")
        except Exception as err:
            return {"exception": repr(err)}
