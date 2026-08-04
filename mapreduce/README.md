# MapReduce Sensor Aggregation

This module demonstrates the Hadoop MapReduce programming model.

## Workflow

Dataset
↓
Mapper
↓
Shuffle & Sort
↓
Reducer
↓
Average Sensor2 Value for each Engine

### Mapper

- Reads engine sensor data
- Emits (Engine ID, Sensor2 Value)

### Reducer

- Groups records by Engine ID
- Calculates average Sensor2 value

### Run

```bash
bash run_mapreduce.sh
```

Example Output

```
1    642.62
2    642.74
3    642.58
...
```
