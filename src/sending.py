'''Classes for sending message by using RabbitMQ'''

import pika
import environ

env = environ.Env()
environ.Env.read_env()


# RabbitMQ connection

params = pika.URLParameters(f"amqp://{env('BROCKER_USER')}:{env('BROCKER_USER')}@{env('BROCKER_HOST')}:{env('BROCKER_PORT')}/")
connection = pika.BlockingConnection(params)
channel = connection.channel()


class SendingForOwner:
    def __init__(self, properties, body):
        channel.basic_publish(exchange='gis', routing_key=properties.headers['owner'], body=f"{body}")

class SendingForService:
    def __init__(self, service, routing_key, body):
        channel.basic_publish(exchange=service, routing_key=routing_key, body=body)


