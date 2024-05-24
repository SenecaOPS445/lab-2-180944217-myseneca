#!/usr/bin/env python3

#Author: Samarth Waghela
#AuthorID: 180944217
#Date Created: 24/5/2024

import sys

if len(sys.argv) != 2:
    print("Usage: {} <timer>".format(sys.argv[0]))
    sys.exit(1)

timer = int(sys.argv[1])

while timer > 0:
    print(timer)
    timer -= 1
print('blast off!')


