# Fault Tolerance

Fault tolerance is achieved using HDFS block replication.

## Workflow

```
Client Upload
      ↓
NameNode
      ↓
Split into Blocks
      ↓
Replicate Blocks
      ↓
Store on Multiple DataNodes
```

If one DataNode fails, Hadoop automatically reads the replicated block from another DataNode.
