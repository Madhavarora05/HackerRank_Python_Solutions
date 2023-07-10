import re
n = int(input())
for i in range(n):
    s = input()
    if len(re.findall(r'[A-Z]',s)) >= 2:
        if len(re.findall(r'[0-9]', s)) >= 3:
            if re.match(r'^[A-Za-z0-9]+$', s):
                if  len(re.findall(r'(.).*\1', s)) == 0:
                    if len(s) == 10:
                        print('Valid')
                        continue
    print('Invalid')