import json

from kafka import KafkaConsumer

bootstrap_server = ["127.0.0.1:19092", "127.0.0.1:29092", "127.0.0.1:19092"]
TOPIC_NAME = "even"

consume = KafkaConsumer(TOPIC_NAME, bootstrap_servers=bootstrap_server)

for index in (json.loads(i.value.decode())["index"] for i in consume):
    print(index)