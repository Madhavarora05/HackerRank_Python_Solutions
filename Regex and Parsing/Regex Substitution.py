import re
def change(match):
    if match.group(1) == '&&':
        return 'and'
    else:
        return 'or'
n=int(input())
for _ in range(n):
    print(re.sub(r"(?<= )(\|\||&&)(?= )", change,input()))