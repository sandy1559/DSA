class node:
    def __init__ (self,data):
        self.data=data
        self.link=None

class linklist:
    def __init__ (self):
        self.head=None

    def additem(self,num):
        if(self.head==None):
            self.head=node(num)
            self.temp=self.head
        else:            
            while(self.temp.link!=None):
                self.temp=self.temp.link
            self.lastnode=node(num)
            self.temp.link=self.lastnode
    
    def displaynodes(self):
        self.x=self.head
        while(self.x!=None):
            print(self.x.data)
            print(self.x)
            self.x=self.x.link
            print(self.x)

    def middlenode(self):
        self.ptr1=self.head
        self.ptr2=self.head
        while(self.ptr2!=None and self.ptr2.link!=None):
            self.ptr1=self.ptr1.link
            self.ptr2=self.ptr2.link.link
           
        print ("middle no is", self.ptr1.data )


obj=linklist()
obj.additem(5)
obj.additem(2)



obj.displaynodes()
obj.middlenode()


