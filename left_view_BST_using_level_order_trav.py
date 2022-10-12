

class bst:
    def __init__ (self,data):
        self.data=data
        self.left=None
        self.right=None

    def insert(self, num):
        if(num<self.data):
            if(self.left!=None):
                self.left.insert(num)
            else:
                self.left=bst(num)
        else:
            if(self.right!=None):
                self.right.insert(num)
            else:
                self.right=bst(num)

    def levelorder(self):
        q=[]
        levels=[]
        q.append(self)
        q.append(None)
        n=len(q)
        while(n!=0):
               if(q[0]!=None): 
                #print(q[0].data, end = " ")
                levels.append(q[0].data)                    #store each node levels in array
               x=q.pop(0)                                   #store pointer of first element

               if(x!=None):
                 if(x.left):                                #store left pointer
                    q.append(x.left)            
                 if(x.right):                               #store right pointer
                    q.append(x.right)       
               if(x==None):
                    #print('\n')
                    q.append(None)
                    levels.append(None)                          #if Null found append another NULL ,i.e we traversed a level
               if(x==q[0]):                                 #if two consecutive NULLS found then traversal is complete and exit loop
                return levels
   
    
def print_left_view(f):                                     #function prints left view nodes of tree using array fetched from levelorder() function
        n=len(f)
        print("Printing Left view of BST....")
        print(f[0])
        for i in range(n-1):                             
            if(f[i]==None):
                print (f[i+1])
   
        

obj=bst(100)
obj.insert(50)
obj.insert(200)
obj.insert(25)

obj.insert(75)
obj.insert(350)
#obj.insert(70)
#obj.insert(80)
f=obj.levelorder()
print_left_view(f)


#Implementaion from https://www.youtube.com/watch?v=NjdOhYKjFrU
