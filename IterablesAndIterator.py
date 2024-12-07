# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations

if __name__ == "__main__":
    listLength = int(input().strip())
    englishLetter = input().strip().split(' ')
    numOfIndices = int(input().strip())

    totalCombinations = list(combinations(englishLetter, numOfIndices))

    # Combinations where 'a' is not present
    no_a_combinations = [combo for combo in totalCombinations if 'a' not in combo]

    # Probability calculation
    probability = (len(totalCombinations) - len(no_a_combinations)) / len(totalCombinations)

    # Print result rounded to 3 decimal places
    print(f"{probability:.3f}")