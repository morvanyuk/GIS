from typing import Any
import environ
import psycopg
import pika

env = environ.Env()
environ.Env.read_env()

class DB_Connecter:

    def __init__(self, *args, **kwds):
        port: int = env('DB_PORT')
        user: str = env('DB_USER')
        host: str = env('DB_HOST')
        password: str = env('DB_PASSWORD')
        db: str = env('DB_NAME')
        
        self.connection = psycopg.connect(dbname=db, user=user, password=password, host=host, port=port)

class Rabbit_Connecter:
  

    def __init__(self):
        port: int = env('BROCKER_PORT')
        user: str = env('BROCKER_USER')
        host: str = env('BROCKER_HOST')

        credentials = pika.PlainCredentials(user, user)
        parameters = pika.ConnectionParameters(host=host, port=port, credentials=credentials)
        self.connection = pika.BlockingConnection(parameters)

database = DB_Connecter().connection
brocker = Rabbit_Connecter().connection
