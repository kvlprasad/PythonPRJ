import time,json,random
from datetime import datetime
from data_generator import generate_message
from kafka3 import KafkaProducer


def serializer(message):
    return json.dumps(message).encode("utf-8");

producer = KafkaProducer(
    bootstrap_servers=["localhost:9092"],
    value_serializer=serializer
    #value_serializer=lambda x: json.loads(x).encode('utf-8')
)

if __name__=="__main__":
    #file = open("/home/kapur/Downloads/SparkStreaming/in/OrderDataArray.json");
    try:
        file = open("resources/cardData.json");

        #while True:
        for line in file.readlines():
            # dummy_messages=generate_message();
            Message=json.loads(line);
            key=str(Message['CardNumber']).encode('utf-8');
            print(f"Producing message {datetime.now()} | Message    = {str(line)}")
            producer.send("demo.cards",value=json.loads(line),key=bytes(key));
            time.sleep(1);
    except Exception as ex:
        print("Exception found :",ex)
    finally:
        file.close()
        producer.flush();