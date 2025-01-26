#!/bin/python3

import math
import os
import random
import re
import sys
from datetime import datetime


# Complete the time_delta function below.
def time_delta(t1, t2):
    # Parse the timestamps using datetime.strptime
    fmt = "%a %d %b %Y %H:%M:%S %z"  # Format string for the timestamp
    dt1 = datetime.strptime(t1, fmt)
    dt2 = datetime.strptime(t2, fmt)

    # Calculate the absolute difference in seconds
    diff = abs((dt1 - dt2).total_seconds())

    # Print the result as an integer
    return str(int(diff))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()
