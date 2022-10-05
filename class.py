class test:
    def __init__ (self,name=None):
        self.vname=name
        print("constructor instantiated wow")
       # print(self.vname)

    def display(self):
        print(self.vname)
       # print(self.obj3.vname)

#test()
obj2=test("2nd name")
obj3=test("3rd name")
obj2.display()

#print(obj2.vname)

