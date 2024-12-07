import numpy
import sys


def read_array_from_args():
    # Read all command-line arguments except the script name
    args = sys.argv[1:]

    if len(args) < 2:
        raise ValueError("Provide at least two values for n and m.")

    # First line gives n and m
    n, m = map(int, args[:2])

    # Validate that enough data points are provided for the array
    expected_values = n * m
    if len(args[2:]) != expected_values:
        raise ValueError(f"Expected {expected_values} values for the array, but got {len(args[2:])}.")

    # Read the next n * m values
    data = list(map(int, args[2:]))

    # Create n x m array
    array = [data[i * m:(i + 1) * m] for i in range(n)]

    return n, m, array

def nummean(arr, ax=1):
    return numpy.mean(arr,axis=ax)

def numvar(arr,ax=0):
    return numpy.var(arr,ax)

def numstd(arr,ax=None):
    return numpy.std(arr,ax)


if __name__ == "__main__":

    n, m = map(int, input().split())
    array = []
    for i in range(n):
        a = list(map(int, input().split()))
        b.append(a)

    array = np.array(b)

    np.set_printoptions(legacy='1.13')


    print(nummean(array))
    print(numvar(array))
    print(numstd(array))