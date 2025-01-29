if __name__ == "__main__":

    n = int(input())
    s = set(map(int, input().split()))

    commandCount = int(input().strip())

    for _ in range(commandCount):
        commandNvalue = input().strip().split()
        command = commandNvalue[0]
        if len(commandNvalue) > 1:
            item = commandNvalue[1]
            getattr(s, command)(int(item))
        else:
            getattr(s, command)()

    sum = 0
    for item in s:
        sum += int(item)
    print(sum)


