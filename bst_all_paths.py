import numpy as np

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



def preorder(root,paths,temp):                          #print all paths using pre order traversal

        temp.append(root.data)    
        
        if(root.left!=None):
           preorder( root.left,paths,temp)       
        if(root.right!=None):
            preorder(root.right,paths,temp)
        if(root.left==None and root.right==None):
            paths=np.array(temp)
            print(paths)
        temp.pop()
        
           
        



obj=bst(100)
root=obj
obj.insert(50)
obj.insert(200)
obj.insert(25)
obj.insert(350)
obj.insert(75)
obj.insert(150)
obj.insert(400)

#obj.insert(70)
#obj.insert(80)
paths=[]
temp=[]
preorder(root,paths,temp)


#https://www.youtube.com/watch?v=gTmtBjv8bo4