from pyspark.sql import SparkSession

# Create a Spark session with Delta Lake configurations
spark = SparkSession.builder \
    .appName("Delta Lake Example") \
    .config("spark.jars.packages", "io.delta:delta-core_2.12:2.2.0") \
    .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
    .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog") \
    .getOrCreate()

# Sample code to read CSV and write to Delta format
def process_data():
    # Read CSV data
    raw_df = spark.read.option("header", "true").option("inferSchema", "true").csv("data/raw/my_raw_file.csv")
    
    # Write to Delta format
    raw_df.write.format("delta").mode("overwrite").save("data/delta/raw/my_table")
    
    # Register as a table
    spark.sql("CREATE TABLE IF NOT EXISTS raw_my_table USING DELTA LOCATION 'data/delta/raw/my_table'")
    
    # Read from Delta table
    delta_df = spark.read.format("delta").load("data/delta/raw/my_table")
    
    # Show the data
    print("Data from Delta table:")
    delta_df.show()

if __name__ == "__main__":
    process_data()
