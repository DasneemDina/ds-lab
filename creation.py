class node:
  def__inite_(self,data)
   self.data=data
   self.next=none 
class linked list:
  def__int_(self):
   self.head=none
  def push(self,new_data):
    new_node=node(new_data)
    new_node.next=self.head
    self.head=new_node
  def insertafter(self,prev_node_new_data):
  if prev_node.node is none:
    print("the given previuos node must in linked list.")
  return
    new_node=node(new data)
    new_node.next=prev_node.next
    prev_node.next=new_node
  def append(self,new_data):
    new_node=node(new_data)
  if self.head is none:
    self.head=new_node
  return
    last=self.head
    while(last.next)
    last=last.next=new_node
  def print list(self):
    temp=self.head
    while(temp):
    print(temp.data)
    temp=temp.next
    if__'name_=='_main_':list
    =linkedkist()
    llist.append(6)
    llist.push(7);
    llist.push(1);
    llist.append(4)
    llist.insertafter (llist.head.next,8)
    print('created linked list is:')
    llist.printlist()
