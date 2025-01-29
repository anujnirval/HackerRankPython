# Enter your code here. Read input from STDIN. Print output to STDOUT


if __name__ == "__main__":
    n, m = input().strip().split()
    array = list(map(int, input().strip().split()))

    happiness = 0

    happySet = set(map(int, input().strip().split()))
    badSet = set(map(int, input().strip().split()))

    for item in array:
        if item in happySet:
            happiness += 1
        elif item in badSet:
            happiness -= 1

    print(happiness)