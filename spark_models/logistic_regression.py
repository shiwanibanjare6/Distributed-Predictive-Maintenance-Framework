from pyspark.sql.functions import when
from pyspark.ml.classification import LogisticRegression
from pyspark.ml.evaluation import MulticlassClassificationEvaluator

df = df.withColumn(
    "failure_label",
    when(col("RUL") <= 30, 1).otherwise(0)
)

ml_df = assembler.transform(df)

train_data, test_data = ml_df.randomSplit([0.8,0.2], seed=42)

lr = LogisticRegression(
    featuresCol="features",
    labelCol="failure_label"
)

lr_model = lr.fit(train_data)

predictions = lr_model.transform(test_data)

accuracy = MulticlassClassificationEvaluator(
    labelCol="failure_label",
    predictionCol="prediction",
    metricName="accuracy"
).evaluate(predictions)

print("Accuracy:", accuracy)
