import psycopg
import pika
import environ
from sending import channel, SendingForOwner, SendingForService
from models import Point, TwoPoints, Restaurant, Order

# Env
env = environ.Env()
environ.Env.read_env()

# params = pika.URLParameters(f"amqp://{env('BROCKER_USER')}:{env('BROCKER_USER')}@{env('BROCKER_HOST')}:{env('BROCKER_PORT')}/")
# connection = pika.BlockingConnection(params)
# channel = connection.channel()

#postgres
conn = psycopg.connect(dbname=env('DB_NAME'), user=env('DB_USER'), 
                        password=env('DB_PASSWORD'), host=env('DB_HOST'), port=env('DB_PORT'))
cursor = conn.cursor()

# Restaurant APIs
'''Adding restaurant point'''
def add_restaurant(ch, method, properties, body):
    data = Restaurant.parse_raw(body)
    # Checking permissions
    cursor.execute(f'''INSERT INTO Restaurants (restaurant_id, restaurant_name, coordinate) VALUES ({data.restaurant_id}, '{data.restaurant_name}', ST_MakePoint({data.coordinate.lat}, {data.coordinate.long}))''')
    conn.commit()
    SendingForOwner(properties=properties, body=200)

'''Removing restaurant point'''
def remove_restaurant(ch, method, properties, body):
    data = int(body)
    # Checking permissions
    cursor.execute(f'''DELETE FROM restaurants WHERE restaurant_id={data}''')
    conn.commit()
    SendingForOwner(properties=properties, body=200)

'''Getting restuarant cooridinate via id'''
def get_restaurant(ch, method, properties, body):
    data = int(body)
    # Checking permissions
    result = cursor.execute(f'''SELECT ST_X(coordinate), ST_Y(coordinate) FROM restaurants WHERE restaurant_id={data}''').fetchone()
    SendingForOwner(properties=properties, body=result)



# Order APIs
'''Adding order'''
def add_order(ch, method, properties, body):
    data = Order.parse_raw(body)
    cursor.execute(f'''INSERT INTO Orders (coordinate, id, restaurant) VALUES (ST_MakePoint({data.coordinate.lat}, {data.coordinate.long}), {data.object_id}, {data.restaurant_id})''')
    conn.commit()
    SendingForOwner(properties=properties, body=200)

'''Removing order'''  
def remove_order(ch, method, properties, body):
    data = int(body)
    cursor.execute(f'''DELETE FROM orders WHERE id={data}''')
    conn.commit()
    SendingForOwner(properties=properties, body=200)

# Other APIs
'''Avalible restaurants for client'''
def in_radius(ch, method, properties, body):
    data = Point.parse_raw(body)
    result = list(cursor.execute(f'''SELECT restaurant_id FROM restaurants WHERE ST_DWithin(coordinate, ST_MakePoint({data.lat}, {data.long}), 15000, TRUE)''').fetchall())
    print(result)
    if len(result) > 0:
        for i in result:
            result[result.index(i)] = list(i)[0]
    SendingForOwner(properties=properties, body=tuple(set(result)))
    
    
if __name__ == '__main__':
    
    channel.basic_consume(queue='add_restaurant', on_message_callback=add_restaurant, auto_ack=True)
    channel.basic_consume(queue='remove_restaurant', on_message_callback=remove_restaurant, auto_ack=True)
    channel.basic_consume(queue='get_restaurant', on_message_callback=get_restaurant, auto_ack=True)
    channel.basic_consume(queue='add_order', on_message_callback=add_order, auto_ack=True)
    channel.basic_consume(queue='remove_order', on_message_callback=remove_order, auto_ack=True)
    channel.basic_consume(queue='radius', on_message_callback=in_radius, auto_ack=True)
    channel.start_consuming()
