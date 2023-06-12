if __name__ == '__main__':
    N = int(input())
    ar=[]
    for _ in range(N):
        choices = input().strip().split(" ")
        func = choices[0]
        if func == "print":
            print(ar)
        elif func == "sort":
            ar.sort()
        elif func == "reverse":
            ar.reverse()
        elif func == "pop":
            ar.pop()
        elif func == "remove":
            val = int(choices[1])
            ar.remove(val)
        elif func == "append":
            val = int(choices[1])
            ar.append(val)
        elif func == "insert":
            pos = int(choices[1])
            val = int(choices[2])
            ar.insert(pos, val)