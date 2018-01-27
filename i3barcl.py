#!/bin/env python3

import sys
import json
import shutil
import os

term_width = shutil.get_terminal_size((80, 20)).columns
count = 0

for line in sys.stdin:
    count += 1
    if count == 5:
        count = 0
    else:
        continue

    oneline = line.replace('\n', '').replace('\r', '')[:-1]
    out = ""
    try:
        j = json.loads(oneline)
        for el in j:
            out += el["full_text"] + " | "
    except ValueError:
        out = "..."
    out = out.center(term_width, ' ')
    os.system('clear')
    print(out)
