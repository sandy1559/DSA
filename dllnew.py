class node:
    def __init__ (self,num):
            self.data=num
            self.left=None
            self.right=None
           # print(self.data,"constrctr done")

class DLL:
    def __init__(self):
            self.head=None

    def insert_at_end(self,num):
        if(self.head==None):
            self.head=node(num)
            self.p=self.head
            return
        else:
            while(self.p.right!=None):
                self.p=self.p.right

        self.q=node(num) 
        self.q.left=self.p
        self.p.right=self.q
        self.p=self.head
        

    def display(self):
        self.p=self.head
        while(self.p!=None):
            print(self.p.data)
            self.p=self.p.right
            
            

obj=node(None)
l1=DLL()
l1.insert_at_end(3)
l1.insert_at_end(6)
l1.insert_at_end(7)
l1.insert_at_end(9)
l1.display()