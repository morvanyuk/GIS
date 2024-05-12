import unittest
from src.models import Point, TwoPoints, Restaurant, Order
import pika
from src.sending import SendingForOwner, SendingForService

from src.sending import channel
 
class TestStringMethods(unittest.TestCase):

    '''Testing Pydantic models'''
    def test_Point(self):
        Point(lat='50.482025338462115', long='30.58368858966708')

    def test_TwoPoints(self):
        TwoPoints(first={'lat' : '50.482025338462115', 'long' : '30.58368858966708'}, 
                  second={'lat' : '50.482025338462115', 'long' : '30.58368858966708'})

    
    '''APIs'''
    def test_in_radius(self):
        channel.basic_publish(exchange='gis', routing_key='radius', body=Point(lat='50.482025338462115', long='30.58368858966708').model_dump_json(),
                              properties=pika.BasicProperties(headers={"owner": "test"}, delivery_mode=2))
    
    
    def test_adding_restaurant(self):
        channel.basic_publish(exchange='gis', routing_key='add_restaurant', 
                              body=Restaurant(restaurant_id=5, coordinate=Point(lat='50.482025338462115', long='30.58368858966708'), restaurant_name='HANAMA').model_dump_json(),
                              properties=pika.BasicProperties(headers={"owner": "test"}, delivery_mode=2))
        
    def test_removing_restaurant(self):
        channel.basic_publish(exchange='gis', routing_key='remove_restaurant',
                               body='5', properties=pika.BasicProperties(headers={"owner": "test"}, delivery_mode=2))
        
    def test_getting_restaurant(self):
        channel.basic_publish(exchange='gis', routing_key='get_restaurant',
                               body='3', properties=pika.BasicProperties(headers={"owner": "test"}, delivery_mode=2))
    def test_adding_order(self):
        channel.basic_publish(exchange='gis', routing_key='add_order',
                               body=Order(restaurant_id=2, object_id=1, coordinate=Point(lat='50.482025338462115', long='30.58368858966708')).model_dump_json(), properties=pika.BasicProperties(headers={"owner": "test"}, delivery_mode=2))
        
    def test_removing_order(self):
        channel.basic_publish(exchange='gis', routing_key='remove_order',
                               body='1', properties=pika.BasicProperties(headers={"owner": "test"}, delivery_mode=2))

if __name__ == '__main__':
    unittest.main()