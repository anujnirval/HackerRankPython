import re

string = input().strip()
substring = input().strip()

pattern = re.compile(substring)

match = pattern.search(string)

while match:
    print(f"({match.start()}, {match.end() - 1})")
    match = pattern.search(string, match.start() + 1)
