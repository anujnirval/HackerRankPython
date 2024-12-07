

def merge_the_tools(string, k):
    substring = []
    p = 0
    for i in range(int(len(string) / k)):
        item = string[p:p+k]
        substring.append(item)
        p+=k
    nextsub = []
    first = ""
    for item in substring:
        for sub in item:
            if sub not in nextsub:
                first = first + sub
                nextsub.append(sub)
        print(first)
        first = ""
        nextsub.clear()



if __name__ == "__main__":
    s = "AABCAAADA"
    k = 3
    merge_the_tools(s, k)
