N=int(input())
arr=input().split()
if all(int(i)>0 for i in arr) and any(i == i[::-1] for i in arr):
    print(True)
else:
    print(False)