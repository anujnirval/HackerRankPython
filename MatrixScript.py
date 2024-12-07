import math
import os
import random
import re
import sys

def single_string(matrix,n,m):
    # print(f"Matrix received: {matrix} and n {n}, m {m}")
    singlestring = []
    for col in range(m):
        for row in range(n):
            # print(f"Now row is {row} and Col is {col} and adding {matrix[row][col]}")
            # print(f"Now complete row is : {matrix[row]}")
            singlestring.append(matrix[row][col])

    singlestring = "".join(singlestring)
    # print(f"Before:{singlestring}")
    pattern = r"(?<=[a-zA-Z0-9])[^a-zA-Z0-9\s]+(?=[a-zA-Z0-9])"
    # print(pattern)
    singlestring = singlestring.replace(" ","*")
    result = re.sub(pattern, " ", singlestring)
    result = result.replace("**","  ")


    print(f"After:{result}")



if __name__ == "__main__":

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    matrix = []

    for i in range(n):
        matrix_item = input()
        matrix.append(matrix_item)

    single_string(matrix,n,m)


