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

Okay, let's structure this comprehensive project into a 20-day learning plan suitable for a GitHub repository. We'll integrate both Flink and Spark components as discussed and provide daily exercises.

---

## GitHub Project Structure Suggestion

```
real-time-data-quality-ai/
├── .github/workflows/         # (Optional) CI/CD actions
├── .gitignore
├── README.md                  # Main project overview, setup, daily plan
├── docker-compose.yml         # The consolidated Docker Compose file
├── data_generator/
│   ├── generate_data.py       # Script to produce Kafka messages
│   └── requirements.txt       # Python dependencies for the generator
├── flink_jobs/
│   ├── flink_stream_processing.py # Basic Flink job (filtering, enrichment)
│   ├── flink_data_quality.py    # Flink job for calculating quality metrics
│   ├── flink_to_cassandra.py    # Flink job writing cleaned data to Cassandra
│   └── requirements.txt       # PyFlink dependencies
├── spark_jobs/
│   ├── spark_data_quality_check.py # Spark batch/streaming quality checks
│   ├── spark_data_cleaning.py   # Spark batch/streaming data cleaning
│   ├── spark_to_cassandra.py    # Spark job writing cleaned data to Cassandra
│   └── requirements.txt       # PySpark dependencies
├── notebooks/
│   ├── 01_Environment_Setup.ipynb # Verify setup, basic connections
│   ├── 02_Kafka_Interaction.ipynb # Interact with Kafka using Python/CLI
│   ├── 03_Flink_Jobs.ipynb        # Submit and monitor Flink jobs
│   ├── 04_Spark_Jobs.ipynb        # Submit and monitor Spark jobs
│   ├── 05_Cassandra_Interaction.ipynb # cqlsh examples, Spark SQL on Cassandra
│   ├── 06_SQL_Analysis.ipynb      # The 10+ complex SQL queries
│   ├── 07_Anomaly_Detection_Conceptual.ipynb # ML concepts, MLflow logging
│   └── 08_Grafana_Setup.ipynb     # Guide for setting up Grafana dashboards
├── ml/
│   ├── model_training_placeholder.py # Placeholder for ML model training
│   └── requirements.txt       # ML dependencies (PyTorch, scikit-learn, mlflow)
├── config/                    # Configuration files (e.g., Cassandra schema)
│   └── cassandra_schema.cql
└── scripts/                   # Helper scripts (e.g., start/stop)
    ├── start_services.sh
    └── stop_services.sh
```

---

## README.md (Enhanced)

```markdown
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
```

```

---

## 20-Day Learning Plan with Daily Exercises

**Day 1: Project Setup & Environment Check**

* **Goal:** Clone the repo, build containers, verify all services are running, and access UIs.
* **Code:** `docker-compose.yml`, `README.md`
* **Exercises (5):**
    1.  Clone the repository successfully.
    2.  Run `docker-compose up -d --build`. List all running containers using `docker ps`. Identify the containers for Kafka, Zookeeper, Flink JobManager, Spark Master, Cassandra, Grafana, MLflow, and Jupyter.
    3.  Access the Flink Web UI (`localhost:8081`). How many TaskManagers are registered? What is the number of available task slots?
    4.  Access the Spark Master Web UI (`localhost:8080`). How many worker nodes are connected? How many cores are available in total?
    5.  Access the Jupyter Notebook environment (`localhost:8888`). Open the `notebooks/01_Environment_Setup.ipynb` notebook and run the cells to confirm basic connectivity checks (e.g., pinging services).

**Day 2: Understanding the Architecture & Docker**

* **Goal:** Understand the flow of data, the role of each component, and basic Docker Compose commands.
* **Code:** `docker-compose.yml`
* **Exercises (6):**
    1.  Draw a diagram illustrating the data flow: Generator -> Kafka -> (Flink/Spark) -> Cassandra -> Grafana/Jupyter/ML. Label each component.
    2.  In `docker-compose.yml`, find the environment variables for Kafka. What do `KAFKA_ADVERTISED_LISTENERS` and `KAFKA_ZOOKEEPER_CONNECT` signify?
    3.  How is the number of Flink TaskManager slots configured in the `docker-compose.yml`? How about the number of Spark worker cores?
    4.  Use `docker logs <container_name>` to view the logs for the `kafka`, `flink-jobmanager`, and `spark-master` services. Look for any startup errors.
    5.  Practice stopping and starting specific services using `docker-compose stop <service_name>` and `docker-compose start <service_name>`. Stop and start the `grafana` service.
    6.  Use `docker-compose down`. What happens to the containers? Run `docker ps` again. Bring the services back up with `docker-compose up -d`.

**Day 3: Data Generation & Kafka Ingestion**

* **Goal:** Understand the data generation script and how data is produced to Kafka. Learn basic Kafka CLI tools.
* **Code:** `data_generator/generate_data.py`, `docker-compose.yml` (data-generator service)
* **Notebook:** `notebooks/02_Kafka_Interaction.ipynb`
* **Exercises (7):**
    1.  Examine `generate_data.py`. What percentage of records are intentionally generated with quality issues? What specific issues are introduced?
    2.  Modify `generate_data.py` to change the frequency of message production (e.g., add a `time.sleep(0.01)`). Restart the `data-generator` container (`docker-compose restart data-generator`).
    3.  Use the Kafka CLI within the Kafka container: `docker exec -it <kafka_container_id> bash`.
    4.  Inside the Kafka container, list the available topics using `kafka-topics --bootstrap-server localhost:9092 --list`. Verify `sensor-topic` exists.
    5.  Use `kafka-console-consumer --bootstrap-server localhost:9092 --topic sensor-topic --from-beginning --max-messages 10` to view the first 10 messages. Can you spot any with quality issues?
    6.  Modify `generate_data.py` to add a new field, e.g., `"status": "active"` for good records and `"status": "error"` for bad ones. Restart the generator and view messages again with the console consumer.
    7.  Complete the exercises in `notebooks/02_Kafka_Interaction.ipynb` to interact with Kafka using a Python client.

**Day 4: Introduction to Flink Stream Processing**

* **Goal:** Submit a basic Flink job to read from Kafka and perform simple filtering. Understand the Flink UI.
* **Code:** `flink_jobs/flink_stream_processing.py`, `flink_jobs/requirements.txt`
* **Notebook:** `notebooks/03_Flink_Jobs.ipynb`
* **Exercises (6):**
    1.  Examine `flink_jobs/flink_stream_processing.py`. What is the purpose of the `JsonRowDeserializationSchema`?
    2.  What filtering logic is applied in this initial Flink job?
    3.  Install PyFlink dependencies inside the Jupyter container (if needed, though the base image might have it). `pip install apache-flink==1.16.0` (match Flink version).
    4.  Submit the Flink job from within the Jupyter notebook using the `!` command or the Python `subprocess` module as shown in `notebooks/03_Flink_Jobs.ipynb`.
    5.  Observe the running job in the Flink UI (`localhost:8081`). Explore the job graph. How many sources, filters, and sinks (print is a sink) are there?
    6.  Modify `flink_stream_processing.py` to add another filter, e.g., filter out records where `sensor_id` is exactly `"sensor_invalid"`. Resubmit the job and verify the change in logs or UI metrics.

**Day 5: Flink Data Quality Metrics**

* **Goal:** Implement a stateful Flink job using `ProcessFunction` to calculate basic data quality metrics.
* **Code:** `flink_jobs/flink_data_quality.py`
* **Notebook:** `notebooks/03_Flink_Jobs.ipynb`
* **Exercises (6):**
    1.  Read `flink_jobs/flink_data_quality.py`. How does the `QualityMetrics` class maintain state (counts of invalid records)?
    2.  What is the role of the `open()` method in a `ProcessFunction`?
    3.  Submit the `flink_data_quality.py` job using the notebook.
    4.  Observe the output printed to the Flink TaskManager logs (`docker logs <flink_taskmanager_container_id>`).
    5.  Modify the `QualityMetrics` class to also count records with missing `sensor_id` (assuming the schema allows nulls or empty strings). Resubmit and check logs.
    6.  **Challenge:** Think about how you would make these metrics more useful. Instead of just printing, where could you send them? (e.g., another Kafka topic, write to a log file, expose via metrics endpoint).

**Day 6: Introduction to Spark & Structured Streaming**

* **Goal:** Use Spark Structured Streaming to read from the same Kafka topic. Compare the approach with Flink.
* **Code:** (Use Spark code directly within the notebook initially)
* **Notebook:** `notebooks/04_Spark_Jobs.ipynb`
* **Exercises (7):**
    1.  In `notebooks/04_Spark_Jobs.ipynb`, initialize a `SparkSession`.
    2.  Write Spark code to read from the `sensor-topic` using the `kafka` format. Define the schema explicitly for the incoming JSON data.
    3.  Parse the JSON value from the Kafka message payload into DataFrame columns.
    4.  Display the streaming DataFrame to the console using `writeStream.format("console").start()`. Observe the output in the notebook.
    5.  Apply a simple filter transformation (e.g., `df.filter("temperature > 20")`) before writing to the console.
    6.  Access the Spark UI (`localhost:8080`). Find your running streaming query under the "Streaming" or "SQL/DataFrame" tabs. Explore the query plan.
    7.  Compare the code structure for reading Kafka in Spark vs. the Flink job from Day 4. What are the main differences in API style?

**Day 7: Spark Data Quality Checks**

* **Goal:** Implement automated data quality checks using Spark DataFrames, similar to the Flink metrics job but using Spark's API.
* **Code:** `spark_jobs/spark_data_quality_check.py`
* **Notebook:** `notebooks/04_Spark_Jobs.ipynb`
* **Exercises (6):**
    1.  Examine `spark_jobs/spark_data_quality_check.py`. How does it calculate counts of invalid records using Spark SQL functions (`when`, `count`)?
    2.  Run this script as a Spark batch job using `spark-submit` from within the Jupyter notebook (or via `docker exec`). Target the `spark-master`.
        ```python
        # In Jupyter cell
        !spark-submit \
            --master spark://spark-master:7077 \
            --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.4.1 \
            /home/jovyan/spark_jobs/spark_data_quality_check.py
        ```
    3.  Adapt the logic from `spark_data_quality_check.py` to work within the streaming query in `notebooks/04_Spark_Jobs.ipynb`. Calculate the quality metrics aggregations over the stream. (Hint: You might need windowing or `flatMapGroupsWithState` for continuous counts, or simply output batch counts).
    4.  Add a new quality check to the Spark script/notebook: Count records where the `sensor_id` does not follow the pattern `sensor_` followed by digits.
    5.  Modify the script to write the quality report DataFrame to a file (e.g., JSON or CSV) instead of just showing it.
    6.  Compare the Spark approach for quality checks with the Flink `ProcessFunction` approach. What are the pros and cons of each?

**Day 8: Data Cleaning with Spark**

* **Goal:** Apply common data cleaning techniques (outlier handling, imputation, validation) using Spark.
* **Code:** `spark_jobs/spark_data_cleaning.py`
* **Notebook:** `notebooks/04_Spark_Jobs.ipynb`
* **Exercises (7):**
    1.  Analyze `spark_jobs/spark_data_cleaning.py`. How are temperature outliers handled? How is humidity imputed?
    2.  What is a Spark UDF (User Defined Function)? Explain the purpose of `sensor_id_check`.
    3.  Integrate the cleaning logic from `spark_data_cleaning.py` into your Spark streaming query in the notebook. Apply the transformations to the Kafka stream.
    4.  Write the *cleaned* streaming DataFrame to the console. Compare its output to the raw stream.
    5.  Experiment with different imputation strategies for humidity (e.g., `median` instead of `mean`). How does the `Imputer` work? (Requires fitting on a batch or historical data first for streaming).
    6.  Implement a fix for the `invalid_timestamp` issue identified in the quality checks (e.g., try parsing, set to null if invalid, or attempt correction).
    7.  **Challenge:** How would you handle records with an invalid `sensor_id` after the UDF validation returns null? Filter them out? Send them to a dead-letter queue (another Kafka topic)?

**Day 9: Introduction to Cassandra**

* **Goal:** Learn basic Cassandra concepts and interact with it using `cqlsh`. Define a schema for sensor data.
* **Code:** `config/cassandra_schema.cql`
* **Notebook:** `notebooks/05_Cassandra_Interaction.ipynb`
* **Exercises (6):**
    1.  Access `cqlsh` within the Cassandra container: `docker exec -it <cassandra_container_id> cqlsh`.
    2.  Create a keyspace for the project (e.g., `iot_data`) using the command provided in `notebooks/05_Cassandra_Interaction.ipynb` or `config/cassandra_schema.cql`. Use `DESCRIBE KEYSPACES;` to verify.
    3.  Examine the `CREATE TABLE` statement in `config/cassandra_schema.cql`. What is the primary key? How does it support time-series data and querying by sensor?
    4.  Create the `sensor_data` table using the statement. Use `DESCRIBE TABLES;` within your keyspace to verify. Use `DESCRIBE TABLE sensor_data;` to see the schema.
    5.  Manually insert a few rows of data using `INSERT INTO iot_data.sensor_data (...) VALUES (...);`.
    6.  Query the inserted data using `SELECT * FROM iot_data.sensor_data WHERE sensor_id = '...' LIMIT 5;`. Try querying by timestamp range as well.

**Day 10: Writing Cleaned Data to Cassandra (Spark)**

* **Goal:** Modify the Spark streaming job to write the cleaned data to the Cassandra table.
* **Code:** `spark_jobs/spark_to_cassandra.py` (or adapt notebook code)
* **Notebook:** `notebooks/04_Spark_Jobs.ipynb`, `notebooks/05_Cassandra_Interaction.ipynb`
* **Exercises (6):**
    1.  You'll need the Spark Cassandra connector. Add the necessary package when submitting the job or configuring the SparkSession: `--packages com.datastax.spark:spark-cassandra-connector_2.12:3.4.1`. Configure the Cassandra connection host: `.config("spark.cassandra.connection.host", "cassandra")`.
    2.  Modify your Spark streaming query (in the notebook or a separate script like `spark_to_cassandra.py`) to write the cleaned DataFrame to Cassandra. Use the `cassandra` format:
        ```python
        cleaned_df.writeStream \
            .format("org.apache.spark.sql.cassandra") \
            .options(table="sensor_data", keyspace="iot_data") \
            .option("checkpointLocation", "/tmp/spark_checkpoint") \ # Required for streaming sinks
            .start()
        ```
    3.  Start the streaming query writing to Cassandra.
    4.  Use `cqlsh` to query the `sensor_data` table. Verify that new data is appearing.
    5.  Check the Spark UI. Observe the query writing to Cassandra. Look at the batch processing times.
    6.  Stop the data generator (`docker-compose stop data-generator`). Does the Spark streaming query stop processing batches? What happens when you restart the generator?

**Day 11: Writing Data to Cassandra (Flink)**

* **Goal:** Implement a Flink job that reads from Kafka, performs basic cleaning/validation, and writes to Cassandra. Compare with the Spark approach.
* **Code:** `flink_jobs/flink_to_cassandra.py`
* **Notebook:** `notebooks/03_Flink_Jobs.ipynb`, `notebooks/05_Cassandra_Interaction.ipynb`
* **Exercises (6):**
    1.  Examine `flink_jobs/flink_to_cassandra.py` (You'll need to create this, potentially using the Flink Cassandra Sink connector). You will likely need to add the connector JAR (`flink-connector-cassandra`) to the Flink image or mount it.
    2.  Add the necessary Flink Cassandra connector dependency (`flink-connector-cassandra_2.12`) to `flink_jobs/requirements.txt` or ensure the JAR is available.
    3.  Define the sink logic in `flink_to_cassandra.py` to map the Flink `DataStream` rows to the Cassandra table columns.
    4.  Submit the `flink_to_cassandra.py` job from the notebook.
    5.  Verify data is being written to Cassandra using `cqlsh`, potentially looking for data processed by Flink (you might add a 'processed_by' field for differentiation).
    6.  Compare the implementation complexity and performance characteristics (observed via UIs) of writing to Cassandra using Flink vs. Spark Structured Streaming for this use case.

**Day 12: Complex SQL Analysis - Part 1**

* **Goal:** Start performing complex data analysis using Spark SQL on the data stored in Cassandra. Focus on aggregations and basic window functions.
* **Notebook:** `notebooks/06_SQL_Analysis.ipynb`
* **Exercises (5):**
    * Ensure you have a good amount of data in Cassandra (let the Spark/Flink writer run for a while).
    1.  In `notebooks/06_SQL_Analysis.ipynb`, load the `sensor_data` table from Cassandra into a Spark DataFrame using the Cassandra connector (`spark.read.format("org.apache.spark.sql.cassandra")...`).
    2.  **Query 1:** Calculate the average, min, and max temperature and humidity for each `sensor_id`.
    3.  **Query 2:** Find the top 10 sensors with the highest number of readings recorded in the last 24 hours. (Requires filtering by timestamp).
    4.  **Query 3:** Calculate the hourly average temperature across *all* sensors. (Hint: Use `hour()` function on timestamp and group by hour).
    5.  **Query 4 (Window Function):** For each sensor, calculate the temperature difference between the current reading and the previous reading (using `LAG`). Order by timestamp.

**Day 13: Complex SQL Analysis - Part 2**

* **Goal:** Continue with more advanced SQL, including CTEs, complex window functions, and pattern detection.
* **Notebook:** `notebooks/06_SQL_Analysis.ipynb`
* **Exercises (5):**
    1.  **Query 5 (CTE & Window):** Use a Common Table Expression (CTE) to first rank sensor readings within each hour, then select the reading with the highest temperature per sensor per hour.
    2.  **Query 6 (Error Rate):** Re-run the query from the prompt: Find sensors with >5% invalid temperature readings (assuming you stored raw data or added a quality flag). Adapt if needed based on your stored schema.
    3.  **Query 7 (Consecutive Spikes):** Implement the query to detect consecutive temperature spikes (>10°C change within 5 minutes) using `LAG` and timestamp differences.
    4.  **Query 8 (Sessionization - Conceptual):** Define a "session" as a period where sensor readings are no more than 15 minutes apart. Write a query to assign a session ID to each reading for a specific sensor. (This is tricky in standard SQL, often involves complex `LAG`/`SUM` over flags).
    5.  **Query 9 (Time-Weighted Average):** Implement the time-weighted average humidity query using `LAG` and `TIMESTAMPDIFF`. Discuss why this might be more accurate than a simple average for unevenly spaced readings.

**Day 14: Introduction to Grafana Visualization**

* **Goal:** Connect Grafana to Cassandra and build basic dashboards to visualize sensor data and quality metrics.
* **Notebook:** `notebooks/08_Grafana_Setup.ipynb` (Guide)
* **Tools:** Grafana UI (`localhost:3000`)
* **Exercises (7):**
    1.  Log in to Grafana (admin/grafana123).
    2.  Add a new Data Source. Select the "Cassandra" data source plugin (it might need to be installed if not included by default in the Grafana image).
    3.  Configure the Cassandra data source connection details (Host: `cassandra:9042`, Keyspace: `iot_data`, default user/pass: `cassandra`/`cassandra` unless changed). Test the connection.
    4.  Create a new Dashboard.
    5.  Add a "Time series" panel. Configure it to query the `sensor_data` table. Select `timestamp` as the time column, `temperature` as a metric column, and potentially group by `sensor_id`. Observe the graph.
    6.  Add another panel showing average humidity over time.
    7.  Add a "Stat" panel showing the total number of records in the table or the latest recorded timestamp.

**Day 15: Visualizing Data Quality in Grafana**

* **Goal:** Enhance Grafana dashboards to specifically monitor data quality aspects.
* **Tools:** Grafana UI, potentially need to write quality metrics to Cassandra/Kafka first.
* **Exercises (6):**
    * *(Prerequisite)* Modify either your Flink or Spark job to write aggregated quality metrics (e.g., count of invalid temps/humidity per sensor per hour) to a *new* Cassandra table (e.g., `sensor_quality_metrics`).
    1.  Create a Cassandra table `sensor_quality_metrics` (e.g., `PRIMARY KEY ((sensor_id, date_hour), timestamp)`) to store hourly quality counts.
    2.  Adapt your Flink/Spark job to aggregate quality issues (like invalid temp/humidity counts) hourly and write them to this new table.
    3.  In Grafana, create a new dashboard focused on Data Quality.
    4.  Add a panel showing the count of invalid temperature readings over time, potentially broken down by sensor_id. Query the `sensor_quality_metrics` table.
    5.  Create a similar panel for invalid humidity readings.
    6.  Add a table panel showing the sensors with the highest error counts in the last hour/day.

**Day 16: Introduction to ML Anomaly Detection & MLflow**

* **Goal:** Understand the concept of anomaly detection for time-series data and use MLflow to log experiment parameters/metrics manually.
* **Code:** `ml/model_training_placeholder.py`, `ml/requirements.txt`
* **Notebook:** `notebooks/07_Anomaly_Detection_Conceptual.ipynb`
* **Tools:** MLflow UI (`localhost:5000`)
* **Exercises (8):**
    1.  Discuss different types of anomalies in sensor data (point anomalies, contextual anomalies, collective anomalies).
    2.  Research two common algorithms for time-series anomaly detection (e.g., Isolation Forest, LSTM Autoencoders, ARIMA). What are their pros and cons?
    3.  Examine `ml/model_training_placeholder.py`. It's a skeleton; how would you load historical data from Cassandra for training?
    4.  In `notebooks/07_Anomaly_Detection_Conceptual.ipynb`, use the `mlflow` Python client.
    5.  Start an MLflow run using `mlflow.start_run()`.
    6.  Log some dummy parameters (e.g., `mlflow.log_param("model_type", "IsolationForest")`, `mlflow.log_param("contamination", 0.05)`).
    7.  Log some dummy metrics (e.g., `mlflow.log_metric("train_accuracy", 0.95)`, `mlflow.log_metric("anomaly_threshold", 0.1)`). End the run.
    8.  Navigate to the MLflow UI (`localhost:5000`). Find your run. Examine the logged parameters and metrics.

**Day 17: Conceptual Model Deployment & Integration**

* **Goal:** Design how a trained anomaly detection model could be integrated into the Flink/Spark pipeline.
* **Notebook:** `notebooks/07_Anomaly_Detection_Conceptual.ipynb`
* **Exercises (5):**
    1.  **Scenario 1 (Spark UDF):** How would you load a trained model (e.g., saved Isolation Forest) and apply it as a UDF in your Spark streaming query to add an `is_anomaly` column? Sketch the code structure.
    2.  **Scenario 2 (Flink Async I/O):** Imagine the model is deployed as a separate microservice (e.g., FastAPI). How could you use Flink's Asynchronous I/O function to call this service for each record in the stream without blocking? Draw the interaction flow.
    3.  **Scenario 3 (Kafka Streams):** Could you deploy the model within a Kafka Streams application that reads from `sensor-topic`, applies the model, and writes results (original data + anomaly score) to a new `anomalies-topic`?
    4.  Discuss the trade-offs (latency, throughput, complexity, state management) between these integration approaches.
    5.  Modify your Flink/Spark job writing to Cassandra to include a placeholder `is_anomaly` boolean column (initially always false).

**Day 18: Pipeline Optimization & Monitoring**

* **Goal:** Use Flink/Spark UIs and system metrics to identify potential bottlenecks and discuss optimization strategies.
* **Tools:** Flink UI, Spark UI, `docker stats`
* **Exercises (7):**
    1.  Run the end-to-end pipeline (Generator -> Kafka -> Flink/Spark -> Cassandra).
    2.  Observe the Flink UI: Check for backpressure between operators. Are any tasks consistently busy? Check checkpointing times and sizes (if configured).
    3.  Observe the Spark UI (Streaming Tab): Look at batch processing times. Are they consistently increasing? Check scheduling delays. Look at task durations and shuffle reads/writes.
    4.  Use `docker stats` in your terminal. Monitor the CPU and Memory usage of the Kafka, Flink TaskManager, Spark Worker, and Cassandra containers. Are any resource-constrained?
    5.  Discuss potential Kafka optimizations: Increase partitions for `sensor-topic`? Adjust replication factor (though it's 1 here)? Change producer/consumer batch sizes?
    6.  Discuss potential Flink/Spark optimizations: Adjust parallelism? Increase TaskManager/Worker memory? Tune serialization? Optimize UDFs? Change checkpointing interval?
    7.  Discuss potential Cassandra optimizations: Review data model/primary key? Tune compaction strategy? Adjust JVM heap settings (already done partially in `docker-compose.yml`)?

**Day 19: Testing & Validation**

* **Goal:** Think about how to test different components of the pipeline.
* **Exercises (6):**
    1.  **Unit Testing:** How would you unit test the data quality rules implemented in your Spark or Flink jobs? (e.g., create sample dataframes/datastreams, apply the logic, assert the output). Sketch a test case for the temperature validation rule.
    2.  **Integration Testing:** How could you test the Kafka -> Flink/Spark -> Cassandra flow? (e.g., produce specific test messages to Kafka, wait, query Cassandra to verify the expected outcome).
    3.  **Load Testing:** How would you simulate higher loads (e.g., >10k msg/sec)? (Modify the generator, potentially run multiple instances, or use dedicated tools like Kafka benchmark tools). What metrics would you monitor?
    4.  **Failure Testing:** What happens if the Cassandra container crashes? Does the Flink/Spark job recover? (Try `docker stop <cassandra_container_id>` while the pipeline is running, then restart it). Does it require checkpointing/WAL?
    5.  What happens if a Flink TaskManager or Spark Worker container fails? Does the system recover? (Try `docker stop <worker_container_id>`).
    6.  How would you validate the end-to-end data integrity? (e.g., compare counts in Kafka vs. Cassandra, checksums).

**Day 20: Documentation & Final Review**

* **Goal:** Improve project documentation and perform a final review of the entire pipeline and learnings.
* **Code:** `README.md`, code comments.
* **Exercises (5):**
    1.  Review the main `README.md`. Is the setup clear? Are the goals well-defined? Is the tech stack accurate? Add any missing details or clarifications.
    2.  Add comments to key sections of your Flink and Spark Python scripts explaining complex logic (e.g., quality rules, windowing, UDFs).
    3.  Create a simple diagram (using text/mermaid in the README or a separate file) illustrating the final pipeline architecture including both Flink and Spark paths.
    4.  Write a short summary (in the README or a separate `CONCLUSIONS.md`) of the key challenges faced during the project and the main learning takeaways.
    5.  Ensure all code is committed to your local Git repository. If this were a real project, what would be the next steps? (e.g., deploying the anomaly model, adding more robust error handling, setting up alerting, integrating Great Expectations).

---
This detailed plan provides a structured path through the project, combining conceptual understanding with hands-on coding and tool interaction. Remember to commit your progress regularly to Git!

---

## Stopping the Services

```bash
docker-compose down -v # Use -v to remove volumes (Cassandra data, Grafana data) if you want a clean restart
