from pyspark.ml.regression import GBTRegressor
from pyspark.ml.evaluation import RegressionEvaluator

gbt = GBTRegressor(
    featuresCol="features",
    labelCol="RUL_capped",
    maxIter=80,
    maxDepth=6,
    stepSize=0.05,
    seed=42
)

gbt_model = gbt.fit(train_data)

predictions = gbt_model.transform(test_data)

rmse = RegressionEvaluator(
    labelCol="RUL_capped",
    predictionCol="prediction",
    metricName="rmse"
).evaluate(predictions)

print("GBT RMSE:", rmse)

gbt_model.write().overwrite().save(
    "hdfs://<MASTER_HOST>:9000/<MODEL_PATH>/final_gbt_model"
)
