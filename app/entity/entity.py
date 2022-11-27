from app.entity.dbconn import DBConn

class Entity:
    _dbInstance = None
    _cache = {}
    _entity_identifier = {}
    _filters = {}
    _df = None

    def __new__(cls):
        cls._dbInstance = DBConn()
        try:
            if cls._instance is None:
                cls._instance = super(__class__, cls).__new__(cls)
            
            return cls._instance
        except:
            return None

    @classmethod
    def _updateCache(cls, key, value = True):
        cls._cache[key] = value

    @classmethod
    def _isCached(cls) -> bool:
        if cls._entity_identifier['key'] in cls._cache:
            return cls._cache[cls._entity_identifier['key']]
        else:
            return False

    @classmethod
    def _primeData(cls):
        print(f"Priming [{cls._entity_identifier['key']}]")
        cls._df = cls._dbInstance.ReadData(spread_sheet_name=cls._entity_identifier['table'], filters=cls._filters)
        cls._updateCache(cls._entity_identifier['key'])

    @classmethod
    def ResetCache(cls):
        try:
            cls._cache[cls._entity_identifier['key']] = False
            return f"Cache Cleared for [{cls._entity_identifier['key']}]"
        except Exception as err:
            return {"exception": err}

