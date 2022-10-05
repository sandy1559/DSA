


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

    def inorder(self):
        if(self.left!=None):
            self.left.inorder()
        print(self.data)
        if(self.right!=None):
            self.right.inorder()
    
    def preorder(self):
        print(self.data)
        if(self.left!=None):
            self.left.inorder()       
        if(self.right!=None):
            self.right.inorder()

    def postorder(self):
        
        if(self.left!=None):
            self.left.inorder()       
        if(self.right!=None):
            self.right.inorder()
        print(self.data)

    def search(self,num):
        if( self.data==num):
            print("node found")
            return
        if(num<self.data):
            if(self.left!=None):
                self.left.search(num)
            else:
                print("node not found")
        else:               
            if(self.right!=None):
                self.right.search(num)
            else:
                print("node not found") 
        




obj=bst(8)
obj.insert(5)
obj.insert(4)
obj.insert(9)
obj.insert(10)
obj.insert(1)
obj.insert(15)
obj.insert(20)
obj.inorder()
obj.preorder()
obj.postorder()
obj.search(1)
#print(obj.right.data)