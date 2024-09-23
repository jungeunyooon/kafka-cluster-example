from confluent_kafka import Producer

def produce_message(producer, topic, message):
    producer.produce(topic, message.encode('utf-8'))
    producer.flush()

def main():
    # kafka IP
    kafka_broker = 'localhost:9092'
    topic = 'stopic'

    # Kafka producer 설정
    producer_config = {
        'bootstrap.servers': kafka_broker,
    }

    # Kafka producer 생성
    producer = Producer(producer_config)

    # 보낼 메시지
    message = "Hello Kafka!"
    print(f"topic : {topic}, meg : {message}")
    produce_message(producer, topic, message)

if __name__ == "__main__":
    main()