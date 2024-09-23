import json
import time

from kafka import KafkaProducer

bootstrap_server = ["127.0.0.1:19092", "127.0.0.1:29092", "127.0.0.1:19092"]
TOPIC_NAME = "additional"

prod = KafkaProducer(bootstrap_servers=bootstrap_server)

num = 0
for i in range(1, 101):
    num += i
    data = {'index': num}
    json_tf = json.dumps(data)
    prod.send(topic=TOPIC_NAME, value=json_tf.encode(encoding='utf-8'))
    # time.sleep(1)
    prod.flush()