a1=int(input())
b1=list(map(int,input().split()))
for i in range(a1):
    b1.sort()
    print(b1[i], end=" ")
