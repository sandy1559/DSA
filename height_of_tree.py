

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

    def maxheight(self,root):
        if(root==None):
            return 0
        lheight=self.maxheight(root.left)
        rheight=self.maxheight(root.right)    
        return (max(lheight,rheight)+1) 

   

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
h=obj.maxheight(root)
print(h)




# https://www.youtube.com/watch?v=9ejFkjEgK3k  ---> Reference