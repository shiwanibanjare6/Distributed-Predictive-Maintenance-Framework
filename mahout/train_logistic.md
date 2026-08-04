# Train Logistic Regression using Mahout

## Prepare Dataset

Merge all CSV parts.

```bash
cat ~/mahout_data/part-* > ~/mahout_data/mahout_final.csv
```

Add column headers.

```bash
echo "failure_label,sensor2,sensor3,sensor4,sensor7,sensor2_avg,sensor3_avg,sensor4_avg,sensor7_avg" \
> ~/mahout_data/mahout_header.csv

cat ~/mahout_data/mahout_final.csv >> ~/mahout_data/mahout_header.csv
```

## Train Model

```bash
mahout trainlogistic \
--input ~/mahout_data/mahout_header.csv \
--output ~/mahout_data/logistic_model \
--target failure_label \
--categories 2 \
--predictors sensor2 sensor3 sensor4 sensor7 sensor2_avg sensor3_avg sensor4_avg sensor7_avg \
--types numeric \
--features 100
```
