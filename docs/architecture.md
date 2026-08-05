# System Architecture

The project follows a master-worker architecture.

```
Client
    ↓
Master Node
(NameNode + ResourceManager + Spark Master)
    ↓
SSH Communication
    ↓
Worker Nodes
(DataNode + NodeManager + Spark Worker)
    ↓
HDFS
    ↓
Spark
    ↓
Prediction
```

The master schedules jobs while worker nodes execute distributed tasks.
