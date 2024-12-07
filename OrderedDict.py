# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict, Counter

if __name__ == "__main__":
    toalItem = int(input().strip())
    items = OrderedDict()

    for _ in range(toalItem):
        name, price = input().rsplit(' ', 1)
        keys = items.keys()
        if name in keys:
            items[name] = int(items[name]) + int(price)
        else:
            items[name] = int(price)

    for it in items:
        print(f"{it} {items[it]}")


