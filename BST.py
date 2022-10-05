

class node:
    def __init__ (self,data):
        self.data=data
        self.left=None
        self.right=None
        
class BST:

    def __init__ (self):
        self.root=None
        
    def insert (self,num):
        if(self.root==None):
            self.root=node(num) #adding 1st node
            self.p=self.root #p points to root
            return

        if(num<self.p.data):
            if (self.p.left==None):
                self.p.left=node(num)
                
            else:
                self.p.left.insert(num)
                
        else:      

            if(num>self.p.data):
                if (self.p.right==None):
                    self.p.right=node(num)
                else:
                    
                    self.p.right.insert(num)

        self.p=self.root #p points to root        

x=node(None)
root=BST()
root.insert(5)
root.insert(4)
root.insert(8)
root.insert(9)


