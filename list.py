list=[1,2,3,4,5,6,8,9,10]
n=len(list)
for i in  range(0,n-1):
    if((list[i+1]-list[i])==1):
        continue
    else:
        print("The misssing no is",list[i]+1)