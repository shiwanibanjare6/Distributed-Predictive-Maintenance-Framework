#!/bin/bash

cat <DATASET_PATH> \
| python3 mapper.py \
| sort \
| python3 reducer.py
