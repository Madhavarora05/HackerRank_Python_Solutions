from itertools import combinations
N=int(input())
Set_N=list(map(str,input().split()))
K=int(input())
comb_list=list(combinations(Set_N,K))
ans_list = [e for e in (comb_list) if "a" in e]
print(len(ans_list) / len(comb_list))
