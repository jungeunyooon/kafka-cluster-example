import json
import time

from kafka import KafkaProducer

bootstrap_server = ["localhost:19094", "localhost:29094", "localhost:39094"]

# bootstrap_server = ["localhost:10001", "localhost:10002", "localhost:10003"]


TOPIC_NAME = "additional"

prod = KafkaProducer(bootstrap_servers=bootstrap_server, acks='all', retries=5)

num = 0
for i in range(1, 101):
    num += i
    data = {'index': num}
    json_tf = json.dumps(data)
    prod.send(topic=TOPIC_NAME, value=json_tf.encode(encoding='utf-8'))
    # time.sleep(1)
    prod.flush()

prod.close()