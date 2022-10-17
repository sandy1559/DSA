

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
        dict={}
        q=[]
        q.append(self)
        q.append(0)                      #add root address & default hight of root(zero) to array
        while(len(q)!=0):
            ptr=q[0]
            level=q[1]                
            q.pop(0)                      #remove first element using pop (pointer)
            q.pop(0)                      #remove 2nd element using pop   (height)
            if not (dict.get(level)):
                dict[level]=ptr.data
            if(ptr.left):                         
                q.append(ptr.left)            #store left pointer address & height to array
                q.append(level-1)      
            if(ptr.right):
                q.append(ptr.right)           #store right pointer address & height to array
                q.append(level+1)      
        return dict 

   





obj=bst(100)
obj.insert(50)
obj.insert(200)
obj.insert(25)
obj.insert(350)
obj.insert(75)
obj.insert(150)
obj.insert(400)
#obj.insert(70)
#obj.insert(80)
top_view=obj.levelorder()
print(top_view)




#https://www.youtube.com/watch?v=EBTku_aIPXk   ---> Reference