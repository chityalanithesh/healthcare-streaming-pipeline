# healthcare-streaming-pipeline
Built a real-time healthcare analytics pipeline using Apache Kafka and Spark Structured Streaming to detect anomalies in patient vitals like oxygen levels and heart rate. Designed for ICU/telehealth use, with support for cloud deployment, alerting, and future ML-driven risk prediction.

# 🏥 Real-Time Healthcare Monitoring Pipeline

This project simulates real-time healthcare data monitoring using Apache Kafka and Spark. It tracks patient vitals (like heart rate, BP), detects anomalies, and generates alerts instantly — enabling faster response in critical care scenarios.

---

## 🔧 Tech Stack
- Apache Kafka
- Apache Spark Structured Streaming
- Python
- Docker & Docker Compose
- Grafana (optional for dashboards)
- Jupyter Notebooks (for data testing)

---

## 📁 Folder Structure

healthcare-streaming-pipeline/
├── docs/ # Architecture diagram
├── configs/ # Kafka config file
├── scripts/
│ ├── kafka/ # Sends simulated vitals
│ └── spark/ # Spark job for alert detection
├── dashboards/ # Optional Grafana dashboard
├── notebooks/ # Data analysis notebook
├── Dockerfile # (Optional) Docker setup
├── docker-compose.yml # Kafka + Spark deployment
└── README.md # This file

---

## 🧪 How It Works

1. Kafka producer simulates patient vitals.
2. Spark Streaming reads the Kafka topic.
3. If abnormal vitals are found, an alert is triggered.
4. Grafana dashboard can show vitals & alerts.

---

## 🚀 How to Run the Project

```bash
# Clone the repo
git clone https://github.com/chityalanithesh/healthcare-streaming-pipeline.git
cd healthcare-streaming-pipeline

# Start services
docker-compose up

# Run Kafka producer
python scripts/kafka/producer.py

# Run Spark streaming job
python scripts/spark/spark_streaming_job.py

