from confluent_kafka import Consumer

# consumer 객체 생성
consumer = Consumer({
    'bootstrap.servers':'localhost:9092',
    'group.id':'test-consumer-group',
    'auto.offset.reset':'earliest'
})
consumer.subscribe(['stopic'])

while True:
    # 단일 메시지를 소비한다.
    # 매개 변수로는 timeout 설정 (float)
    message = consumer.poll(1.0)
    if message:
        print('Received message: {}'.format(message.value().decode('utf-8')))
    else:
        continue

consumer.close()