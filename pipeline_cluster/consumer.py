import json

from kafka import KafkaConsumer

from kafka import KafkaProducer

bootstrap_server = ["127.0.0.1:19092", "127.0.0.1:29092", "127.0.0.1:19092"]
TOPIC_NAME = "additional"
ODD_TOPIC = "odd"
EVEN_TOPIC = "even"

consume = KafkaConsumer(TOPIC_NAME, bootstrap_servers=bootstrap_server)
prod = KafkaProducer(bootstrap_servers=bootstrap_server)


def deliver_number(n: int) -> bool:
    return True if n % 2 == 0 else False


for index in (json.loads(i.value.decode())["index"] for i in consume):
    topic_trans = EVEN_TOPIC if deliver_number(index) else ODD_TOPIC
    data = {'index': index}
    prod.send(topic=topic_trans, value=json.dumps(data).encode(encoding='utf-8'))
    print(topic_trans, deliver_number(index), index)
    prod.flush()