import environ
import psycopg
import pika

env = environ.Env()
environ.Env.read_env()

class DB_Connecter:
    port: int = env('DB_PORT')
    user: str = env('DB_USER')
    host: str = env('DB_HOST')
    password: str = env('DB_PASSWORD')
    db: str = env('DB_NAME')

    @property
    def connection(self, *args, **kwds):
        conn = psycopg.connect(dbname=self.db, user=self.user, password=self.password, host=self.host, port=self.port)
        return conn

class Rabbit_Connecter:
    port: int = env('BROCKER_PORT')
    user: str = env('BROCKER_USER')
    host: str = env('BROCKER_HOST')

    @property
    def connection(self, *args, **kwds):
        params = pika.URLParameters(f"amqp://{self.user}:{self.user}@{self.host}:{self.port}/")
        connection = pika.BlockingConnection(params)
        return connection

db = DB_Connecter()
brocker = Rabbit_Connecter()

print(db, brocker)