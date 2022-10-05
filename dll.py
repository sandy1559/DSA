class node:                                    #double linked list
    def __init__ (self,data):
        self.data=data
        self.left=None
        self.right=None
        print(self.data,"constrctr done")

class DLL:
    def __init__  (self):
        self.head=None

    def insert(self,num):
        
        if(self.head==None):                   #if linked list empty  
            self.head=node(num)
            self.p=self.head                   #pointer p used for traversing to last node
        while(self.p.right!=None):
            self.p=self.p.right
            print(self.p)

        self.q=node(num)
        self.q.left=self.p                    #pointer q used for creating new node  
        self.p.right=self.q
        

    def display(self):
        self.p=self.head   
        while(self.p!=None):
            print(self.p.data, " ")
            self.p=self.p.right
        

obj=node(None)
l1=DLL()
l1.insert(3)
l1.insert(6)
l1.insert(9)
l1.insert(11)
l1.display()
