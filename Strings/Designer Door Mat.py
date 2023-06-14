N, M = map(int, input().split())
x= ( ( M - 3 ) // 2 )
for i in range(1,N,2):
    print("-" * x + ".|." * i + "-" * x)
    x-=3
print("-"*((M-7)//2),"WELCOME","-"*((M-7)//2),sep="")
x=3
for i in range(N-2,0,-2):
    print("-" * x + ".|." * i + "-" * x)
    x+=3