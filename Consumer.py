from kafka import KafkaConsumer
from kafka.errors import KafkaError

def main():
    consumer = KafkaConsumer(bootstrap_servers='localhost:9092', auto_offset_reset='earliest')
    consumer.subscribe(['test'])

    for message in consumer:
        print (message.value)


if __name__ == '__main__':
    main()