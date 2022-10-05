
class bst:
    def __init__ (self,data):
        self.data=data
        self.lchild=None
        self.rchild=None

    def insert(self,num):
        if(self.data==None):
            self.data=num
            return

        if(num<self.data):
            if self.lchild:
                self.lchild.insert(num)
            else:                
                self.lchild=bst(num)
        else:            
            if self.rchild:
                self.rchild.insert(num)                
            else:
                self.rchild=bst(num)

    def preorder(self):
        
        if self.lchild:
            self.lchild.preorder()
        print(self.data, end=" ")
        if self.rchild:
            self.rchild.preorder()

    def countnodes(self):
            if(self.data==None):
             return 0
            else:
                n= 1+self.lchild.countnodes()+self.rchild.countnodes()
                return n

        
            



root=bst(11)
print(root.lchild)
print(root.data)
print(root.rchild)

list1=[9,13,8,10,12,14,15,7]
for i in list1:
    root.insert(i)

root.preorder()
x=root.countnodes()
print(x)