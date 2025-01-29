import numpy as np


def diagonalDifference(ar):
    # Write your code here
    ar = np.array(ar)
    first = sum(np.diagonal(ar))
    second = sum(np.diagonal(np.fliplr(ar)))
    return abs(first-second)

if __name__== "__main__":
    arr = input()
    diagonalDifference(arr)
