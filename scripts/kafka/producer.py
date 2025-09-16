
from kafka import KafkaProducer
import json
import random
import time

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def generate_patient_data():
    return {
        "patient_id": random.randint(1, 100),
        "heart_rate": random.randint(60, 120),
        "oxygen_level": round(random.uniform(85, 100), 2),
        "temperature": round(random.uniform(36.0, 39.0), 2)
    }

while True:
    data = generate_patient_data()
    print("Sending:", data)
    producer.send("patient-vitals", value=data)
    time.sleep(1)
