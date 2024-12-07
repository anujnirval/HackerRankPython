from itertools import groupby

if __name__ == "__main__":

    s = input().strip()
    results = []

    for char, group in groupby(s):
        count = len(list(group))
        results.append(f"({count}, {char})")

    print(' '.join(results))