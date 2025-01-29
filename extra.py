from math import floor

sets = set(map(int,input().split()))
lst = [3,4,5,6,1,7]
if sets in lst:
    print(sets)
else:
    print("No")

for item in sets:
    print(int(item))

for value,j in enumerate(lst):
    print (value,j)

print(int(6/2))

floor()