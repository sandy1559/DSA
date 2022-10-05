
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
            if(self.lchild==None):
                self.lchild=bst(num)
            else:
                self.lchild.insert(num)
        else:            
            if(self.rchild==None):
                self.rchild=bst(num)
            else:
                self.rchild.insert(num)

    def preorder(self):
        
        if(self.lchild!=None):
            self.lchild.preorder()
        print(self.data, end=" ")
        if(self.rchild!=None):
            self.rchild.preorder()

def countnodes(self):
    if(self==None):
        return 0
    else:
        n= 1+countnodes(self.lchild)+countnodes(self.rchild)
    return n


root=bst(11)
list1=[9,13,8,10,12,14,15]
for i in list1:
    root.insert(i)

root.preorder()
print("no of nodes is ", countnodes(root))
#x=root.countnodes()
#print(x)