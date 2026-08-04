from pyspark.sql.functions import max, col, when, avg
from pyspark.sql.window import Window

# Generate RUL
rul_df = df.groupBy("engine_id") \
    .agg(max("cycle").alias("max_cycle"))

df = df.join(rul_df, on="engine_id", how="left")

df = df.withColumn(
    "RUL",
    col("max_cycle") - col("cycle")
)

# Cap RUL
df = df.withColumn(
    "RUL_capped",
    when(col("RUL") > 125, 125).otherwise(col("RUL"))
)

# Rolling Window
window_spec = Window.partitionBy("engine_id") \
    .orderBy("cycle") \
    .rowsBetween(-5, 0)

# Rolling Average Features
df = df.withColumn("sensor2_avg", avg("sensor2").over(window_spec))
df = df.withColumn("sensor3_avg", avg("sensor3").over(window_spec))
df = df.withColumn("sensor4_avg", avg("sensor4").over(window_spec))
df = df.withColumn("sensor7_avg", avg("sensor7").over(window_spec))

print("Feature Engineering Completed")
df.show(5)
