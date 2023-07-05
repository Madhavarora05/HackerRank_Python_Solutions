from itertools import combinations_with_replacement

S,K = input().split()
K = int(K)
S = sorted(S)
for i in combinations_with_replacement(S, K):
    print("".join(i))