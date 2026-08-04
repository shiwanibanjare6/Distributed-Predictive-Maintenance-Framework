# Mahout Commands

## Verify Installation

```bash
mahout
```

## Create Dataset

```bash
mkdir -p ~/mahout_data
```

## Download Dataset from HDFS

```bash
hdfs dfs -get <HDFS_DATASET_PATH>/part-* ~/mahout_data/
```

Example

```bash
hdfs dfs -get \
/predictive-maintenance/mahout_dataset/part-* \
~/mahout_data/
```

## Merge Files

```bash
cat ~/mahout_data/part-* > ~/mahout_data/mahout_final.csv
```
