class node:
def__init_(self,dataval=none):
self.dataval=dataval
self.nextval=none
class slinked list:
def__init_(self):
self.headval=none
deflistprint (self):
printval is not none:
print(printval.dataval)
printval=printval.nextval
defatbegining(self,new data):
new node=node(new data)
new node.nextvalself.headval
self.headval=newnode
list=slinkedlist()
list.headval=node("mon")
e2=node("tue")
e3=node("wed")
list.headval.nextval=e2
e2.nextval=e3
list.atbegining("sun")
list.print()
