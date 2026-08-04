#  Distributed Predictive Maintenance Framework using Hadoop and Spark Ecosystem

![Python](https://img.shields.io/badge/Python-3.8-blue?logo=python)
![Apache Spark](https://img.shields.io/badge/Apache%20Spark-3.5.1-orange?logo=apachespark)
![Hadoop](https://img.shields.io/badge/Hadoop-3.3.6-yellow?logo=apachehadoop)
![Hive](https://img.shields.io/badge/Apache%20Hive-3.1.3-brown)
![Mahout](https://img.shields.io/badge/Apache-Mahout-green)
![License](https://img.shields.io/badge/License-MIT-blue)

A scalable **Big Data predictive maintenance framework** built on the Hadoop ecosystem for **Remaining Useful Life (RUL) prediction** and **engine failure classification**. The project combines distributed storage, parallel processing, feature engineering, and machine learning using a **multi-node Hadoop-Spark cluster**.

---

## 📖 Overview

Modern industrial systems continuously generate massive volumes of sensor data. Traditional single-machine solutions struggle with scalability, storage, and computation when processing such datasets.

This project presents a **distributed predictive maintenance framework** that integrates Hadoop and Spark technologies to efficiently process industrial sensor data, predict engine health, estimate Remaining Useful Life (RUL), and classify potential failures.

Unlike conventional machine learning projects, this framework emphasizes **distributed computing, fault tolerance, and parallel processing**, making it suitable for large-scale industrial analytics.

---

## ✨ Key Features

- Multi-node Hadoop cluster (1 Master + 3 Worker Nodes)
- Distributed storage using HDFS
- Fault-tolerant architecture with HDFS replication
- Spark-based distributed preprocessing and feature engineering
- Hive SQL analytics over distributed datasets
- Custom MapReduce implementation for sensor aggregation
- Distributed machine learning using Spark MLlib
- Mahout-based distributed Logistic Regression
- RUL prediction and engine failure classification
- Parallel execution across Spark workers

---

## 🏗️ System Architecture

> **(Add your architecture diagram here)**

The framework consists of the following layers:

```
Client
    ↓
Master Node
(NameNode + ResourceManager + Spark Master)
    ↓
SSH Communication
    ↓
Worker Nodes
(DataNodes + Spark Workers)
    ↓
HDFS Distributed Storage
    ↓
Hive Analytics + MapReduce
    ↓
Spark Distributed Processing
    ↓
Feature Engineering
    ↓
Machine Learning Models
    ↓
Prediction Results
```

---

## 🛠️ Technology Stack

### Big Data

- Apache Hadoop 3.3.6
- HDFS
- YARN
- Apache Spark 3.5.1
- Apache Hive 3.1.3
- Apache Mahout
- MapReduce

### Machine Learning

- Spark MLlib
- Gradient Boosted Trees
- Random Forest
- Linear Regression
- Logistic Regression

### Programming

- Python
- PySpark
- HiveQL
- Linux Shell

---

## 📂 Dataset

**NASA Turbofan Engine Degradation Simulation Dataset (CMAPSS)**

Dataset includes:

- Multiple engine units
- Operational settings
- 21 sensor measurements
- Engine degradation cycles

Target variables:

- Remaining Useful Life (RUL)
- Engine Failure Classification

---

## ⚙️ Methodology

### 1. Distributed Data Storage

- Uploaded datasets into HDFS
- Block replication across DataNodes
- Fault-tolerant storage

### 2. Distributed Analytics

- Hive external tables
- SQL analytics
- MapReduce sensor aggregation

### 3. Feature Engineering

- RUL Generation
- RUL Capping
- Rolling Sensor Averages
- Failure Label Creation

### 4. Distributed Machine Learning

- Linear Regression
- Random Forest
- Gradient Boosted Trees
- Logistic Regression
- Mahout Logistic Regression

### 5. Model Evaluation

- RMSE
- Accuracy
- F1 Score

---

## 📊 Results

### Regression Models

| Model | RMSE |
|--------|------:|
| Linear Regression | 44.86 |
| Random Forest | 41.50 |
| Gradient Boosted Trees | **18.19** |

---

### Classification Model

| Metric | Score |
|---------|-------:|
| Accuracy | **94.69%** |
| F1 Score | **94.69%** |

---

## 🖥️ Distributed Cluster Configuration

| Component | Configuration |
|------------|---------------|
| Master Node | 1 |
| Worker Nodes | 3 |
| HDFS | ✔ |
| YARN | ✔ |
| Spark Cluster | ✔ |
| Hive | ✔ |
| MapReduce | ✔ |
| Mahout | ✔ |

---

## 📁 Project Structure

```
Distributed-Predictive-Maintenance-Framework/

├── architecture/
├── cluster_setup/
├── datasets/
├── hive/
├── mahout/
├── mapreduce/
├── preprocessing/
├── spark_models/
├── results/
├── paper/
├── presentation/
└── README.md
```

---

## 🚀 Big Data Components Implemented

- Multi-node Hadoop Cluster
- HDFS Distributed Storage
- Block Replication
- Fault Tolerance
- Spark Distributed Processing
- Hive Analytics
- MapReduce
- Mahout
- Spark MLlib
- Parallel Machine Learning

---

## 📈 Future Enhancements

- Real-time streaming using Apache Kafka
- Kubernetes deployment
- Docker containerization
- IoT sensor integration
- Deep Learning-based RUL prediction
- Cloud deployment on AWS or Azure

---

## 📄 Research Paper

This project has been documented in IEEE research paper format covering:

- Distributed Cluster Architecture
- Hadoop Ecosystem Integration
- Spark-Based Machine Learning
- MapReduce Processing
- Hive Analytics
- Mahout Classification
- Experimental Evaluation

---

## 👩‍💻 Author

**Shiwani Banjare**

B.Tech – Data Science and Artificial Intelligence

Indian Institute of Information Technology Naya Raipur

---

## ⭐ If you found this project useful, consider giving it a star!
