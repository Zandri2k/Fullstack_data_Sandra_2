from database import DatabaseDataFrame
from constants import DATA_PATH

class QueryDatabase:
    def __init__(self, sql_query) -> None:
        with DatabaseDataFrame(DATA_PATH) as db:
            self.db = db.query(sql_query)