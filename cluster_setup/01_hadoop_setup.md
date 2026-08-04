# Hadoop Cluster Setup

## Configure Hosts

Edit `/etc/hosts` on every node.

```text
172.16.xx.xx master
172.16.xx.xx slave1
172.16.xx.xx slave2
172.16.xx.xx slave3
```

## Configure Workers

Edit:

```text
$HADOOP_HOME/etc/hadoop/workers
```

```
slave1
slave2
slave3
```

## Generate SSH Key

```bash
ssh-keygen
```

Copy to workers:

```bash
ssh-copy-id slave1
ssh-copy-id slave2
ssh-copy-id slave3
```
