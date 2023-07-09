import re
n = int(input())
for _ in range(n):
    number=input()
    cond = re.compile(r"^[7-9]\d{9}$")
    if bool(re.match(cond, number)):
        print("YES")
    else:
        print("NO")