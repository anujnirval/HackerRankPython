from itertools import product

if __name__ == "__main__":
    # Input values
    k, m = map(int, input().split())  # Number of lists (k) and modulo value (m)

    lists = []
    for _ in range(k):
        line = list(map(int, input().split()))
        lists.append(line[1:])  # Exclude the size of the list

    # Generate all combinations using product
    combinations = product(*lists)

    # Calculate the maximum value of the given equation
    max_value = 0
    for combination in combinations:
        current_value = sum(x ** 2 for x in combination) % m
        max_value = max(max_value, current_value)

    print(max_value)