import re
v = "aeiou"
c = "qwrtypsdfghjklzxcvbnm"
s=input()
m = re.findall(r"(?<=[%s])([%s]{2,})[%s]" % (c, v, c), s, flags = re.I)
print('\n'.join(m or ['-1']))