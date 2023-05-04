import mysql.connector
from mysql.connector import errorcode

"""
Simple Database Handler
"""


class DBHandler:
    def __init__(self, config):
        self.config = config

    def connect(self):
        try:
            self.cnx = mysql.connector.connect(**self.config)

            self.cursor = self.cnx.cursor()
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
        else:
            return self

    def insert(self, query, data):
        self.query(query, data)

    def remove(self, query, data):
        self.query(query, data)

    def update(self, query, data):
        self.query(query, data)

    def query(self, query, data=None):
        try:
            self.cursor.execute(query, data)
            self.cnx.commit()
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_CLIENT_QUERY_FAILURE_INVALID_NON_ROW_FORMAT:
                print("There is an error in query")
            else:
                print(err)

    def fetch_all(self, query):
        try:
            self.cursor.execute(query)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_CLIENT_QUERY_FAILURE_INVALID_NON_ROW_FORMAT:
                print("There is an error in query")
            else:
                print(err)
        else:
            return self.cursor.fetchall()