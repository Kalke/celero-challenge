import os
import pandas as pd
import psycopg2
from sqlalchemy import create_engine

class UploadDatabase:
    def __init__(self):

        self.__username = 'postgres'
        self.__password = '2009'
        self.__host = 'localhost'
        self.__port = '5432'
        self.__db = 'celero'
        self.__schema = 'public'
        
    def table_exists(self,table_str):
        conn = psycopg2.connect(f"dbname={self.__db} user={self.__username} host={self.__host} password={self.__password}")
        exists = False
        try:
            cur = conn.cursor()
            cur.execute("select exists(select relname from pg_class where relname='" + table_str + "')")
            exists = cur.fetchone()[0]
            cur.close()
        except psycopg2.Error as e:
            print(e)
        return exists

    def upload_data(self, path):
        for item in os.listdir(path):
            table = pd.read_csv(path+item)
            item = item.replace('.csv','')
            if self.table_exists(item) == False:
                print(f'Uploading {item}...')
                self.__engine = create_engine(f'postgresql+psycopg2://{self.__username}:{self.__password}@{self.__host}:{self.__port}/{self.__db}')
                table.to_sql(name = item, con = self.__engine,
                                        schema = self.__schema, if_exists = 'replace',
                                        index = False, chunksize = 10)
                print(f'Table {item} uploaded.')
                return True
            else:
                print(f'Table {item} already exists.')
                pass