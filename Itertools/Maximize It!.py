import itertools
K,M=map(int,input().split())
N=[]
for i in range(K):
    arr = list(map(int, input().split()))
    N.append(arr[1:])
all_comb = itertools.product(*N)
ans = 0
for single_comb in all_comb:
    ans = max(sum(x * x for x in single_comb) % M, ans)
print(ans)