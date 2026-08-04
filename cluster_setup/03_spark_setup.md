# Spark Cluster

## Start Spark Master

```bash
start-master.sh
```

## Start Spark Workers

```bash
start-workers.sh spark://master:7077
```

## Launch PySpark

```bash
pyspark --master spark://master:7077
```
