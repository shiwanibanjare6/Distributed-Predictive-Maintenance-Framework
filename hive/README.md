# Hive Analytics

Apache Hive was used to perform SQL-based analytics on data stored in HDFS.

## Operations Performed

- Created Database
- Created External Table
- Loaded Dataset from HDFS
- Aggregation Queries
- Filtering
- Group By Operations
- Statistical Analysis

## Sample Commands

```sql
SHOW TABLES;

SELECT * FROM train_fd001 LIMIT 10;

SELECT AVG(sensor2)
FROM train_fd001;
```

Hive translates SQL queries into distributed execution jobs, allowing efficient analysis of large datasets stored in HDFS.
