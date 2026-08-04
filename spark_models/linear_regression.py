from pyspark.ml.feature import VectorAssembler
from pyspark.ml.regression import LinearRegression
from pyspark.ml.evaluation import RegressionEvaluator

# Feature Columns
feature_cols = [
    "op_setting1","op_setting2","op_setting3",
    "sensor1","sensor2","sensor3","sensor4",
    "sensor5","sensor6","sensor7","sensor8",
    "sensor9","sensor10","sensor11","sensor12",
    "sensor13","sensor14","sensor15","sensor16",
    "sensor17","sensor18","sensor19","sensor20",
    "sensor21"
]

assembler = VectorAssembler(
    inputCols=feature_cols,
    outputCol="features"
)

ml_df = assembler.transform(df)

train_data, test_data = ml_df.randomSplit([0.8,0.2], seed=42)

lr = LinearRegression(
    featuresCol="features",
    labelCol="RUL"
)

model = lr.fit(train_data)

predictions = model.transform(test_data)

rmse = RegressionEvaluator(
    labelCol="RUL",
    predictionCol="prediction",
    metricName="rmse"
).evaluate(predictions)

print("RMSE:", rmse)
