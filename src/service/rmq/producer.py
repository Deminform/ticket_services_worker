import pika

from datetime import datetime
import json
from src.settings.config import settings


def get_channel():
    print(settings.rmq_login, settings.rmq_password)
    credentials = pika.PlainCredentials(settings.rmq_login, settings.rmq_password)
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(
            host=settings.rmq_host,
            port=settings.rmq_port,
            credentials=credentials))
    channel = connection.channel()

    channel.exchange_declare(exchange='notify', exchange_type='direct')
    channel.queue_declare(queue='email_queue', durable=True)
    channel.queue_bind(exchange='notify', queue='email_queue')
    return channel


def send_notification(email, message):
    data = {
            "email": email,
            "payload": message,
            "date": datetime.now().isoformat()
        }
    channel = get_channel()
    channel.basic_publish(
        exchange='notify',
        routing_key='email_queue',
        body=json.dumps(data).encode(),
        properties=pika.BasicProperties(
            delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
            ))
    print(" [x] Sent %r" % data)
