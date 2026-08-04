#!/usr/bin/env python3

import sys

current_engine = None
total = 0
count = 0

for line in sys.stdin:
    engine_id, value = line.strip().split("\t")
    value = float(value)

    if current_engine == engine_id:
        total += value
        count += 1
    else:
        if current_engine:
            print(f"{current_engine}\t{total/count}")

        current_engine = engine_id
        total = value
        count = 1

if current_engine:
    print(f"{current_engine}\t{total/count}")
