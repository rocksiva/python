a,b=map(int,input().split())
for i in range(a,b):
    tem=0
    x=i
    while x>0:
        dig=(x%10)**3
        tem=tem+dig
        x=x//10
    if (i==tem):
        print(i)
