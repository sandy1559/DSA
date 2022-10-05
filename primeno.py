

n=8
cnt=1
list=[2]
num=2

while len(list)<=n:
    if(n==1):
        break
    if(n==len(list)):
        break
    else:
        num=num+1
        if(num%2==0 or num%3==0):
           cnt=1
           continue
        else:
            list.append(num)
            cnt=1
            continue
print(list)
