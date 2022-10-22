

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

def min_node(ptr):
    if(ptr.left!=None):
        return min_node(ptr.left)
    else:
        return ptr.data    

def max_node(ptr):
    if(ptr.right!=None):
        return max_node(ptr.right)
    else:
        return ptr.data  
    



obj=bst(100)
root=obj
obj.insert(50)
obj.insert(200)
obj.insert(25)
obj.insert(350)
obj.insert(75)
obj.insert(150)
obj.insert(400)
obj.insert(60)
obj.insert(80)
x=min_node(root)
y=max_node(root)
print("Minimum element in tree is ",x)
print("Maximum element in tree is ",y)
