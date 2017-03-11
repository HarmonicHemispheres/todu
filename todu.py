#!/usr/bin/env python3

import sys

def get_tasks(file):
    return read(open(file, "r"))

# ========== MAIN ========== 

a = get_tasks(sys.args[1])
print(a)

