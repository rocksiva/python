a=int(input())
num=a
tem=0
while num>0:
    dig=(num%10)**3
    tem=tem+dig
    num=num//10
    
if a==tem:
    print("yes")
else:
    print("no")
    
    
    
