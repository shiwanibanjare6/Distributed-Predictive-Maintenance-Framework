from pyspark.sql import SparkSession
from pyspark.sql.functions import max, col, when

# Create Spark Session
spark = SparkSession.builder.appName("<PROJECT_NAME>").getOrCreate()

# Read Dataset
df = spark.read.option("inferSchema", "true") \
    .option("sep", " ") \
    .csv("hdfs://<MASTER_HOST>:9000/<HDFS_DATASET_PATH>")

# Remove Empty Columns
df = df.drop("_c26", "_c27")

# Rename Columns
columns = [
    "engine_id", "cycle",
    "op_setting1", "op_setting2", "op_setting3",
    "sensor1", "sensor2", "sensor3", "sensor4",
    "sensor5", "sensor6", "sensor7", "sensor8",
    "sensor9", "sensor10", "sensor11", "sensor12",
    "sensor13", "sensor14", "sensor15", "sensor16",
    "sensor17", "sensor18", "sensor19", "sensor20",
    "sensor21"
]

df = df.toDF(*columns)

print("Dataset Loaded Successfully")
df.show(5)
