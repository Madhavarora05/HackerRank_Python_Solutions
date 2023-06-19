Set_A=set(map(int, input().split()))
n=int(input())
for _ in range(n):
    Other_Set=set(map(int,input().split()))
    print(Set_A.issuperset(Other_Set))
