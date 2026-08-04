from pyspark.ml.regression import RandomForestRegressor
from pyspark.ml.evaluation import RegressionEvaluator

rf = RandomForestRegressor(
    featuresCol="features",
    labelCol="RUL_capped",
    numTrees=50,
    maxDepth=10,
    seed=42
)

rf_model = rf.fit(train_data)

rf_predictions = rf_model.transform(test_data)

rmse = RegressionEvaluator(
    labelCol="RUL_capped",
    predictionCol="prediction",
    metricName="rmse"
).evaluate(rf_predictions)

print("Random Forest RMSE:", rmse)
