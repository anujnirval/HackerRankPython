def findZigZagSequence(a, n):
    a.sort()
    mid = int((n + 1) / 2)
    a[mid-1], a[n - 1] = a[n - 1], a[mid-1]
    print(a)
    lastHalf = a[mid:]

    lastHalf.sort(reverse=True)
    print(lastHalf)

    a[mid:mid+len(lastHalf)] = lastHalf
    print(a)

if __name__ == "__main__":
    s = input().strip().split()
    n = len(s)
    findZigZagSequence(s,n)