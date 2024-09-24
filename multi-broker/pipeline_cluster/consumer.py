import json

from kafka import KafkaConsumer

from kafka import KafkaProducer

bootstrap_server = ["localhost:19094", "localhost:29094", "localhost:39094"]

TOPIC_NAME = "additional"
ODD_TOPIC = "odd"
EVEN_TOPIC = "even"

consume = KafkaConsumer(
    TOPIC_NAME,
    bootstrap_servers=bootstrap_server,
    group_id='my-consumer-group',
    auto_offset_reset='earliest',
    # consumer_timeout_ms=10000  # 10초 동안 메시지가 없으면 종료
)
prod = KafkaProducer(bootstrap_servers=bootstrap_server)


def deliver_number(n: int) -> bool:
    return True if n % 2 == 0 else False

for index in (json.loads(i.value.decode())["index"] for i in consume):
    try:
        topic_trans = EVEN_TOPIC if deliver_number(index) else ODD_TOPIC
        data = {'index': index}
        prod.send(topic=topic_trans, value=json.dumps(data).encode(encoding='utf-8'))
        print(topic_trans, deliver_number(index), index)
        prod.flush()
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
    except Exception as e:
        print(f"Error processing message: {e}")


consume.close()