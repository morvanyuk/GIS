'''Classes for sending message by using RabbitMQ'''

from connections import brocker

# RabbitMQ
channel = brocker.channel()

class SendingForOwner:
    def __init__(self, properties, body):
        channel.basic_publish(exchange='gis', routing_key=properties.headers['owner'], body=f"{body}")

class SendingForService:
    def __init__(self, service, routing_key, body):
        channel.basic_publish(exchange=service, routing_key=routing_key, body=body)


