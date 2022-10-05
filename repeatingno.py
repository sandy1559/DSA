list=[8,1,12,4,2,5,8,7,8,8,8,8]

n=len(list)

def rep_no():
    count=0
    repno=None    
    for i in range(0,n-1):
        
        for j in range(0,n-1):
        
            if list[i]==list[j]:
                count=count+1
        
        if(count>1):
            print(count+1)
            repno=list[i]
            break
        else:
            count=0
    
    return repno
        
x=rep_no()        
print ("The repeating no in array is ", x)
