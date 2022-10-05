list=[8,1,12,4,2,5,8,7,8,8,8,8]
unqlist=[]
n=len(list)

def find_unique():
    for i in range(0,n-1):
        if(i==0):
            unqlist.append(list[i])
        else:
            m=is_checked(list[i])
            if(m==1):
                continue
            else:
                 unqlist.append(list[i])   
    print (unqlist)

def is_checked(x):
    checked=0
    for j in range(0,len(unqlist)-1):
        if(x==unqlist[j]):
            checked=1
            break
    return checked

find_unique()
