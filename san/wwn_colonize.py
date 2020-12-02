#!/usr/bin/env python3

import sys

for wwn in sys.stdin:
    wwn = ':'.join([wwn[i:i+2] for i in range(0, len(wwn)-1, 2)])
    print(wwn)
