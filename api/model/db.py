# import mysql.connector
import os
from supabase import create_client, Client
class DatabaseConnection:
    _instance = None
    #override new when DatabaseConnection()
    def __new__(cls, *args, **kwargs):  #is a special method in Python that is considered as one of the class constructors
        

        #in the context of the __new__ method, cls refers to the class itself. Specifically, it is the class that the method is called on. In the line cls._instance = super(DatabaseConnection, cls).__new__(cls, *args, **kwargs) is an instance of the DatabaseConnection class.
        if not cls._instance:
            
            #same as calling object._new(...) so new Object(ofType(cls) which is DatabaseConnection)
            cls._instance = super(DatabaseConnection, cls).__new__(cls, *args, **kwargs)
          
            # Initialize database connection 
            # cls._instance.connection = mysql.connector.connect(
            #     host='127.0.0.1',
            #     user='root',
            #     password='password',
            #     database='clothes'
            # )
            url: str = os.environ.get("SUPABASE_URL")
            key: str = os.environ.get("SUPABASE_KEY")
            supabase: Client = create_client(url, key)


            cls._instance.client = supabase

        return cls._instance
    
    # The Database class defines the `get_connection` method that lets
    # clients access the same instance of a database connection
    # throughout the program.
    def get_client(self):
        return self.client

test = DatabaseConnection()