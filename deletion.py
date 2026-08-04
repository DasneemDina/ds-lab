class node:
  def__init_(self,data=none):
  self.data=data
  self.next=none
class slinked list:
def__init_(self):
self.head=none
defatbegining(self,data_in):
newnode=node(data_in)
new node.next=self head
self.head=newnode
def removenode(self,removekey):
  headval=selfself.head
  if(headval.data==removekey):
    headval=self.head
    if(headval.data==removekey):
      self.head=headval.next
      headval=none
      return
      while(headval is not none):
        if headval.data==removekey:
          break
          prev=headvalheadval
          =headval.nextin
          (headval==none):
          return
          prev.next=headval.next
          headval=none
          defllistprint(self):
          printval=self.head
          while(printval):
            print(printval.data)
            printval=printval.next
            llist=sliunkedlist()
            llist.atbegining("mon")
            llist.atbegining("tue")
            llist.atbegining("wed")
            llist.atbegining("thu")
            llist.removenode("tue")
            llist.llistprint()
