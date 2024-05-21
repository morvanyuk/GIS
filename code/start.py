from connections import brocker

channel = brocker.channel()

channel.exchange_declare(exchange='gis', exchange_type='direct', auto_delete=False)

channel.queue_declare('radius', durable = False)
channel.queue_declare('test', durable = False)
channel.queue_declare('add_restaurant', durable = False)
channel.queue_declare('remove_restaurant', durable = False)
channel.queue_declare('get_restaurant', durable = False)
channel.queue_declare('add_order', durable = False)
channel.queue_declare('remove_order', durable = False)

channel.queue_bind(queue='radius', exchange='gis', routing_key='radius')
channel.queue_bind(queue='test', exchange='gis', routing_key='test')
channel.queue_bind(queue='add_restaurant', exchange='gis', routing_key='add_restaurant')
channel.queue_bind(queue='remove_restaurant', exchange='gis', routing_key='remove_restaurant')
channel.queue_bind(queue='get_restaurant', exchange='gis', routing_key='get_restaurant')
channel.queue_bind(queue='add_order', exchange='gis', routing_key='add_order')
channel.queue_bind(queue='remove_order', exchange='gis', routing_key='remove_order')

brocker.close()
