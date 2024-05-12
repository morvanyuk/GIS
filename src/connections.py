import psycopg
import environ

# pg_dsn: PostgresDsn = 'postgres://user:pass@localhost:5432/foobar'
# amqp_dsn: AmqpDsn = 'amqp://user:pass@localhost:5672/'

env = environ.Env()
environ.Env.read_env()

class DB_Connecter:
    port: int = env('DB_PORT')
    user: str = env('DB_USER')
    host: str = env('DB_HOST')
    password: str = env('DB_PASSWORD')
    db: str = env('DB_NAME')

    # @property
    # def url(self):
    #     return f'postgres://{self.user}:{self.password}@{self.host}:{self.port}/{self.db}'

    conn = psycopg.connect(dbname=env('DB_NAME'), user=env('DB_USER'), 
                        password=env('DB_PASSWORD'), host=env('DB_HOST'), port=env('DB_PORT'))
    
    @property
    def connection(self, *args, **kwds):
        conn = psycopg.connect(dbname=self.db, user=self.user, password=self.password, host=self.host, port=self.port)
        return conn

db_config = DB_Connecter()
print(db_config.connection)