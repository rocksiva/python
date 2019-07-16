list1=""
(a,b)=map(int,(input()).split())
for i in range(a,b):
    if i==1:
        continue
    if i%2!=0:
        list1=list1+str(i)+" "
print(list1)
