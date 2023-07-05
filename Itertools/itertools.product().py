from itertools import product
A=list(map(int,input().split()))
B=list(map(int,input().split()))
ans=list(product(A,B))
for i in ans:
    print(i,end=" ")