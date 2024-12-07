# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict, Counter

if __name__ == "__main__":
    n = int(input())
    words = OrderedDict()
    count = 1

    for _ in range(n):
        word = input().strip()
        if word in words.keys():
            words[word] = words[word] + 1
        else:
            words[word] = 1

    ctr = Counter(words)
    print(len(ctr))
    ls = []
    for items in words:
        ls.append(ctr[items])
    print(*ls)



