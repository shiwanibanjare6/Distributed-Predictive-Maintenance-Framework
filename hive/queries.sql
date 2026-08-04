-- Show Tables
SHOW TABLES;

-- Display Dataset
SELECT * FROM train_fd001 LIMIT 10;

-- Total Records
SELECT COUNT(*) FROM train_fd001;

-- Number of Engines
SELECT COUNT(DISTINCT engine_id)
FROM train_fd001;

-- Average Sensor2 Value
SELECT AVG(sensor2)
FROM train_fd001;

-- Maximum Cycle of Each Engine
SELECT engine_id,
MAX(cycle)
FROM train_fd001
GROUP BY engine_id;

-- Average Sensor2 per Engine
SELECT engine_id,
AVG(sensor2)
FROM train_fd001
GROUP BY engine_id
LIMIT 10;
