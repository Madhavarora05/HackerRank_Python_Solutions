from itertools import permutations
S,K=list(map(str, input().split(" ")))
S=sorted(S)
ans=list(permutations(S,int(K)))
for i in ans:
    for j in i:
        print(j,end="")
    print()


# Or it can be printed like this

# for p in list(itertools.permutations(s, int(n))):
#     print("".join(p))