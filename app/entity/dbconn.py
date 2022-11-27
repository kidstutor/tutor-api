import pandas as pd
import numpy as np
from app.db.dbgoogle import GoogleSheet

class DBConn():
    _dbInstance = None

    def __new__(cls):
        try:
            if cls._dbInstance is None:
                cls._dbInstance = GoogleSheet()
            return cls._dbInstance
        except:
            return None

    @property
    def dbInstance(self):
        return self._dbInstance

# class DBGoogle(DBConn):
