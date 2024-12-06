

def merge_the_tools(string, k):
    subString = []
    p = 0
    for i in range(int(len(string) / k)):
        item = string[p:p+k]
        subString.append(item)
        p+=k
    nextSub = []
    first = ""
    for item in subString:
        for sub in item:
            if sub not in nextSub:
                first = first + sub
                nextSub.append(sub)
        print(first)
        first = ""
        nextSub.clear()



if __name__ == "__main__":
    s = "AABCAAADA"
    k = 3
    merge_the_tools(s, k)
