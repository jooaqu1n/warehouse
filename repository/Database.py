import pymysql
pymysql.install_as_MySQLdb() 
import MySQLdb
from typing import List

class Database:

    #--------------------------------------------------------------
    def __init__(self, user: str, passwd: str, host: str, db: str):
        self.__user: str = user
        self.__passwd: str = passwd
        self.__host: str = host
        self.__db: str = db

    #--------------------------------------------------------------
    def connect(self) -> None:
        self.__connection = MySQLdb.connect(user = self.__user, passwd = self.__passwd, host = self.__host, db = self.__db)

    #--------------------------------------------------------------
    def close(self):
        self.__connection.close()

    #--------------------------------------------------------------
    def getRecords(self, query: str) -> List:
        cursor = self.__connection.cursor()
        cursor.execute(query)
        data = cursor.fetchall()        
        return data

    #--------------------------------------------------------------
    def getRecord(self, query: str) -> object:
        cursor = self.__connection.cursor()
        cursor.execute(query)
        data = cursor.fetchall()        
        return data[0]