a1=int(input())
b1=list(map(int,input().split()))
if (len(b1)==a1):
    b1.sort()
    for i in range(a1):
        print(b1[i], end=" ")
