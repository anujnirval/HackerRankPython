#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'gridChallenge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY grid as parameter.
#

def gridChallenge(grid):
    # Write your code here
    row = len(grid)
    cols = len(grid[0])
    for i in range(len(grid)):
        lst = list(grid[i])
        lst.sort()
        grid[i] = (''.join(lst))

    col = []
    result = "NO"
    for i in range(cols):
        for j in range(row):
            col.append(grid[j][i])
        existing = col[:]
        col.sort()
        if existing == col:
            result = "YES"
        else:
            result = "NO"
            break
        col = []
    return str(result)

    print(grid)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(grid)

        fptr.write(result + '\n')

    fptr.close()
