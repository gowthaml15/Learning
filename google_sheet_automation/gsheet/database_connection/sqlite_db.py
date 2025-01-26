import sqlite3
import pandas as pd

class SQLite:
    def __init__(self,db_loc:str,db_query:str):
        self.db_loc = db_loc
        self.db_query = db_query
        self.conn = self.get_conn()
    
    def get_conn(self):
        conn = sqlite3.connect(self.db_loc)
        return conn

    def get_query_output(self):
        df = pd.read_sql_query(self.db_query,self.conn)
        self.conn.close()
        return df
    

