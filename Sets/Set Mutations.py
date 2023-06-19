A=int(input())
Set_A=set(map(int,input().split()))
N=int(input())
for i in range(N):
    choice=list(input().split())
    cmd=choice[0]
    updated_set=set(map(int,input().split()))
    if cmd=='intersection_update':
        Set_A.intersection_update(updated_set)
    elif cmd=='update':
        Set_A.update(updated_set)
    elif cmd=='symmetric_difference_update':
        Set_A.symmetric_difference_update(updated_set)
    else:
        Set_A.difference_update(updated_set)
print(sum(Set_A))