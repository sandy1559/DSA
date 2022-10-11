

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
        q.append(self)                      #add root address to array
        while(len(q)!=0):
            print(q[0].data)                
            x=q.pop(0)                      #remove first element using pop
            if(x.left):                         
                q.append(x.left)            #store left pointer address  to array
            if(x.right):
                q.append(x.right)           #store right pointer address to array
          

   

   
        




obj=bst(10)
obj.insert(20)
obj.insert(30)
obj.insert(40)
obj.insert(50)
obj.insert(60)
obj.insert(70)
obj.insert(80)
obj.levelorder()

#print(obj.right.data)
#kjhkjhkjh