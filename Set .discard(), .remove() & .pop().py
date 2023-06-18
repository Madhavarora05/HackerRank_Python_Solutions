n = int(input())
s = set(map(int, input().split()))
N=int(input())
for i in range(N):
    x= list(map(str, input().split()))
    if len(x)==1:
        s.pop()
    else:
        cmd=x[0]
        value=int(x[1])
        if cmd=='discard':
            s.discard(value)
        else:
            s.remove(value)
print(sum(s))
        