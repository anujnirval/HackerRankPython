from collections import deque

if __name__ == "__main__":
    numTest = int(input().strip())  # Number of test cases

    results = []  # To store results for each test case

    for _ in range(numTest):
        numCubes = int(input().strip())  # Number of cubes
        cubes = deque(map(int, input().strip().split()))  # List of cube lengths

        possible = "Yes"  # Assume it's possible until proven otherwise
        top = float("inf")  # Initially, no cube is stacked, so top is very large

        while cubes:
            # Compare the leftmost and rightmost cubes
            if cubes[0] >= cubes[-1]:
                selected = cubes.popleft()  # Take the leftmost cube
            else:
                selected = cubes.pop()  # Take the rightmost cube

            # Check if the selected cube can be stacked
            if selected > top:
                possible = "No"
                break
            top = selected  # Update the top cube

        results.append(possible)

    # Print all results
    print("\n".join(results))