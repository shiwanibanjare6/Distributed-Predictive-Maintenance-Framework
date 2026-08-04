#!/usr/bin/env python3

import sys

for line in sys.stdin:
    data = line.strip().split()

    if len(data) < 8:
        continue

    engine_id = data[0]
    sensor2 = float(data[6])

    print(f"{engine_id}\t{sensor2}")
