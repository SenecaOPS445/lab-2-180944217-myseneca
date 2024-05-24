#!/usr/bin/env python3

#Author: Samarth Waghela
#AuthorID: 180944217
#Date Created: 24/5/2024

import sys

if len(sys.argv) > 1:
     timer = int(sys.argv[1])
else:
    timer = 3

while timer > 0:
    print(timer)
    timer -= 1
print('blast off!')


