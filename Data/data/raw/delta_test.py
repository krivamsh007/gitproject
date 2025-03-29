from pyspark.sql import SparkSession

# Create Spark session pointing to the Spark master
spark = SparkSession.builder \
    .appName("DeltaTest") \
    .master("spark://spark-master:7077") \
    .getOrCreate()

# Read a CSV file from /home/jovyan/work/data/raw (adjust filename as needed)
df = spark.read.option("header", "true") \
    .option("inferSchema", "true") \
    .csv("/home/jovyan/work/data/raw/my_raw_file.csv")

# Write to Delta
df.write.format("delta").mode("overwrite") \
    .save("/home/jovyan/work/delta/raw/my_table")

spark.sql("""
    CREATE TABLE IF NOT EXISTS raw_my_table
    USING DELTA
    LOCATION '/home/jovyan/work/delta/raw/my_table'
""")

# Query the table
spark.sql("SELECT * FROM raw_my_table LIMIT 10").show()

spark.stop()
