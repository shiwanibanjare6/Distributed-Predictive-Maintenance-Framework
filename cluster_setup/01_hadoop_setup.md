# Hadoop Cluster Setup

## 1. Configure Hosts

Edit `/etc/hosts` on every node.

```text
<MASTER_IP>    master
<SLAVE1_IP>   slave1
<SLAVE2_IP>   slave2
<SLAVE3_IP>   slave3
```

Example:

```text
172.16.xx.xx master
172.16.xx.xx slave1
172.16.xx.xx slave2
172.16.xx.xx slave3
```

---

## 2. Configure Hadoop Workers

Edit:

```text
<HADOOP_HOME>/etc/hadoop/workers
```

Add:

```text
slave1
slave2
slave3
```

---

## 3. Generate SSH Key

```bash
ssh-keygen
```

Press **Enter** for all default options.

---

## 4. Copy SSH Key to Worker Nodes

```bash
ssh-copy-id <USERNAME>@slave1
ssh-copy-id <USERNAME>@slave2
ssh-copy-id <USERNAME>@slave3
```

Example:

```bash
ssh-copy-id bigdata@slave1
```
