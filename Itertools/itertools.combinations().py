from itertools import combinations
S,K=list(map(str, input().split(" ")))
S=sorted(S)
K=int(K)+1
for i in range(1,K):
    for j in combinations(S,i):
        for k in j:
            print(k,end="")
        print()
 
# IT can also be printed like this
   
# for i in range(1, K):
#     for j in combinations(s, i):
#         print("".join(j))