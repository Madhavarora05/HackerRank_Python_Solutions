M=int(input())
a=set(map(int,input().split()))
N=int(input())
b=set(map(int,input().split()))
a_diff = a.difference(b)
b_diff = b.difference(a)
for i in sorted(a_diff.union(b_diff)):
    print(i)