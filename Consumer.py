from kafka import KafkaConsumer
from kafka.errors import KafkaError


consumer = KafkaConsumer(bootstrap_servers='localhost:9092', auto_offset_reset='earliest')
consumer.subscribe(['test'])

for message in consumer:
    print (message)