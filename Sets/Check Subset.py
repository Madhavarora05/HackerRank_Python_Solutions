T=int(input())
for _ in range(T):
    A=int(input())
    Set_A=set(map(int,input().split()))
    B=int(input())
    Set_B=set(map(int,input().split()))
    print(Set_A.issubset(Set_B))

