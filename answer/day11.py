#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

max_sum = 0
tmp_sum = 0

for i in range(4):
    for j in range(4):
        tmp_sum = arr[i][j] + arr[i][j+1] + arr[i][j+2]
        tmp_sum += arr[i+1][j+1]
        tmp_sum += arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
        if i == 0 and j == 0:
            max_sum = tmp_sum
        if tmp_sum > max_sum:
            max_sum = tmp_sum
print(max_sum)
