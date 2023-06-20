import math
ab=float(input())
bc=float(input())
ac=math.sqrt(ab**2 + bc**2)
theta=math.acos(bc/ac)
print(int(round(math.degrees(theta),0)),chr(176),sep="")