N ,X =map(int,input().split())
marks=[]
for _ in range(X):
    marks.append(list(map(float,input().split())))
for i in zip(*marks):
    print("{0:.1f}".format(sum(i)/X))