class node:
    def __init__ (self,data) :
        self.data=data
        self.next=None
        print("in constructor")

class linklist:
    
    def __init__(self):
        self.head=None

    def append(self,num):
        if(self.head==None):
            print("list is empty")
            self.head=node(num)
            self.p=self.head
            print(self.head, "head node addr")
        else:
            while(self.p.next!=None):
                   self.p=self.p.next
            self.lastnode=node(num)
            self.p.next=self.lastnode  
    def display(self):
            self.t=self.head
            while(self.t!=None):
                print(self.t.data)
                print(self.t)
                self.t=self.t.next
                print(self.t)
            print(self.head, "compare head addr")
    def deletenode(self,numx):
        self.temp=self.head
        while(self.temp!=None):
            
            if(self.head.data==numx):
                self.head=self.head.next
                print("first node is deleted and head pointed to 2nd node")
                break
            else:           
                self.temp1=self.temp
                self.temp=self.temp.next    
                if((self.temp) and (self.temp.data==numx)):
                    self.temp1.next=self.temp.next
                
            #self.temp=self.temp.next

#obj=node()
l1=linklist()
l1.append(2)
l1.append(3)
l1.append(6)
l1.append(8)
l1.append(10)
l1.append(15)
l1.deletenode(15)
l1.display()
