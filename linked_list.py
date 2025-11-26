#linked list:to over come dis advantages of list and array
#what is an array=homogenius collection of elements
#dose list and array in python same?=no
#collecton of limited homogenius elements,all datatypes should be same
#collection of homogenius elements,can have diff datatypes
#major diff b/w list and array is array is fixed size
# list memory allocation is continuous memory location ame for array tooo,what if the memory avalible is dispached?
#so we use linked list where each patch contains data and address of the next patch(node).
#disadvantage of linked lsit=can not move back word uni way travarsel and it can not be indexed

#simple code
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
head=Node(5)
# n2=Node(-4)#still no connection between them
# head.next=n2#connection estlablisned
# n3=Node(25)
# n2.next=n3

def Didplay_linked_list(head):
    if head == None:
        return "empty list"
    temp=head
    while temp != None:
        print(temp.data,end=" ")
        temp= temp.next
    print()
#Didplay_linked_list(head1)

#function to add node at the start
def Add_Node_At_Start(head,new_node_data):
    if head == None:
        new_node=Node(new_node_data)
        head = new_node
        return head
    else:
        new_node=Node(new_node_data)
        new_node.next=head
        head = new_node
        print("Added at the Start successfully")
        return head
#function to add node at the end
def Add_Node_At_End(head,new_node_data):
    if head == None:
        new_node=Node(new_node_data)
        head = new_node
        return head
    else:
        temp=head
        new_node=Node(new_node_data)
        while temp.next != None:
            temp = temp.next
        temp.next=new_node
        print("Added at the end Successfully")
        return head

#function to delete node at the specific point
def Delete_At_Specific(head,del_data):
    if head == None:
        print("list is empty")
        return head
    if head.data == del_data:
        head = head.next
        return head
    else:
        temp=head
        previous=None
        while temp is not None and temp.data != del_data:
                previous = temp
                temp = temp.next
        if temp is None:
            print("no node with that data")
            return head
        if temp.next == None:
            previous.next = None
            return head
        else: 
            previous.next = temp.next 
            return head
def Reverse_List(head):
    if head == None:
        return 'empty list'
    elif head.next ==None:
        return head
    else:
        prev=None
        current=head
        next=None
        while current != None:
            next= current.next
            current.next=prev
            prev = current
            current=next
        return prev
        

head=Add_Node_At_Start(head,6)
head=Add_Node_At_End(head,10)
head=Add_Node_At_End(head,20)
#head=Delete_At_Specific(head,20)
head=Reverse_List(head)
Didplay_linked_list(head)






# def add_at_the_end(head,new_data):
#     if head == None:
#         return 'empty list'
#     temp=head
#     while temp.next != None:
#         temp = temp.next
#     new_node=Node(new_data)
#     temp.next.next=new_node











