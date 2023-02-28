import json
from kafka3 import KafkaConsumer

if __name__=="__main__":

    consumer=KafkaConsumer(
        "demo.cards",
        bootstrap_servers="localhost:9092",
        auto_offset_reset="latest"
    )

    for msg in consumer:
        JsonObj=json.loads(msg.value);
        print("Key :" + str(msg.key));

        print(type(JsonObj));
        print(json.dumps(JsonObj,indent=1))
        # load will deserilize the json str to json dict Object.
        #