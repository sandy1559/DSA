#Sum of the nodes of BST

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

    def sumofnodes(self,root):
        if(root==None):
            return 0
        sum=root.data+self.sumofnodes(root.left)+self.sumofnodes(root.right)
        return sum    
    
    

   
        

obj=bst(100)
root=obj                        #1st node is root, hence saving pointer in root variable
obj.insert(50)
obj.insert(200)
obj.insert(25)

obj.insert(75)
obj.insert(350)
#obj.insert(70)
#obj.insert(80)

sumx=obj.sumofnodes(root)
print("The sum of nodes is ", sumx)