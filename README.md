# Real-Time Data Quality Monitoring with AI

## Overview

This project implements an end-to-end data pipeline for ingesting, processing, validating, and analyzing streaming data in real-time. It demonstrates the use of both Apache Flink and Apache Spark for stream/batch processing, identifies data quality issues, cleans the data, stores it in Cassandra, and uses AI concepts for anomaly detection. The entire infrastructure is containerized using Docker Compose.

**Goal:** Provide a hands-on learning experience covering data engineering, data quality, stream processing, big data tools, basic AI integration, and systems design within a realistic context.

## Learning Outcomes

* **Data Engineering:**
    * High-volume data ingestion with Kafka.
    * Stream processing concepts with Apache Flink (filtering, stateless/stateful operations).
    * Batch and micro-batch processing with Apache Spark (Structured Streaming, DataFrames).
    * Data storage strategies with NoSQL databases (Cassandra time-series modeling).
    * Schema validation and data enrichment techniques.
* **Data Quality:**
    * Identifying common data quality issues (missing values, outliers, incorrect types, invalid formats).
    * Implementing automated data quality checks in Flink and Spark.
    * Applying data cleaning techniques (imputation, capping, validation).
* **SQL & Analysis:**
    * Writing complex SQL queries for data profiling and analysis (Window Functions, CTEs, Aggregations).
    * Performing analysis using Spark SQL on data stored in Cassandra.
* **AI Integration:**
    * Understanding the workflow for training and deploying anomaly detection models.
    * Using MLflow for experiment tracking (conceptual).
    * Integrating model predictions (conceptually) into the pipeline.
* **Infrastructure & Systems Design:**
    * Orchestrating multi-container applications with Docker Compose.
    * Understanding resource allocation and monitoring for distributed systems (Flink UI, Spark UI, Grafana).
    * Comparing and contrasting Flink and Spark for different use cases.
    * Building monitoring dashboards with Grafana.

## Tech Stack

* **Orchestration:** Docker, Docker Compose
* **Data Ingestion:** Apache Kafka
* **Stream Processing:** Apache Flink (PyFlink)
* **Batch/Stream Processing:** Apache Spark (PySpark)
* **Storage:** Apache Cassandra
* **Data Quality:** Custom logic in Flink/Spark (can integrate libraries like Great Expectations later)
* **AI/ML:** PyTorch/Scikit-learn (conceptual), MLflow (tracking)
* **Visualization:** Grafana
* **Development:** Jupyter Notebooks, Python

## Setup Instructions

1.  **Prerequisites:**
    * Git ([https://git-scm.com/downloads](https://git-scm.com/downloads))
    * Docker & Docker Compose ([https://docs.docker.com/get-docker/](https://docs.docker.com/get-docker/)) - Ensure Docker has sufficient resources allocated (e.g., 8GB+ RAM, 4+ CPUs recommended).
2.  **Clone the Repository:**
    ```bash
    git clone <your-repo-url>
    cd real-time-data-quality-ai
    ```
3.  **Build and Start Services:**
    ```bash
    docker-compose up --build -d
    ```
    *(This may take several minutes the first time as images are downloaded.)*
4.  **Verify Services:**
    * Check running containers: `docker ps`
    * Access Web UIs:
        * Flink UI: `http://localhost:8081`
        * Spark Master UI: `http://localhost:8080`
        * Jupyter Notebook: `http://localhost:8888` (Token might be needed from `docker logs <jupyter-container-id>`)
        * Grafana: `http://localhost:3000` (Default user/pass: admin/grafana123 - defined in `docker-compose.yml`)
        * MLflow UI: `http://localhost:5000`
5.  **Run Data Generator:**
    *(The `data-generator` service in `docker-compose.yml` should start automatically. Verify logs if needed)*
    ```bash
    docker logs -f real-time-data-quality-ai-data-generator-1 # (Adjust container name if needed)
    ```
6.  **Access Jupyter Notebooks:** Navigate to `http://localhost:8888` and explore the `notebooks/` directory, starting with `01_Environment_Setup.ipynb`.

## 20-Day Learning Plan & Exercises

Follow the daily plan below. Each day includes exercises designed to be completed within Jupyter notebooks or using terminal commands interacting with the Docker containers.

---

**(Daily Plan Below)**

---

## Stopping the Services

```bash
docker-compose down -v # Use -v to remove volumes (Cassandra data, Grafana data) if you want a clean restart
