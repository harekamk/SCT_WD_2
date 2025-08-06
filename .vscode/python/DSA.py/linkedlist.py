# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# class LinkedList:
#     def __init__(self):
#         self.head=None
#     def front(self,data):
#         new_node=Node(data)
#         new_node.next=self.head
#         self.head=new_node
#     def last(self,data):
#         new_node=Node(data)
#         if not self.head:
#             self.head=new_node
#         else:
#             curr=self.head
#             while curr.next:
#                 curr=curr.next
#             curr.next=new_node
#     def print_list(self):
#         curr=self.head
#         while curr:
#             print(curr.data,end="->")
#             curr=curr.next
#         print("none")

# linked_list=LinkedList()

# linked_list.front(10)
# linked_list.front(20)
# linked_list.front(30)
# linked_list.last(40)
# linked_list.last(50)

# linked_list.print_list()
     
#search for 7
'''class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
        #front
    def front(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node
        
    def search(self,data):
        curr=self.head
        idx=0
        while curr:
            if curr.data==data:
                return idx
            curr=curr.next
            idx+=1
        return -1
            #print
    def print_list(self):
        curr=self.head
        while curr:
            print(curr.data,end="->")
            curr=curr.next
        print("null")


linked_list=LinkedList()    
linked_list.front(3)
linked_list.front(2)
linked_list.front(8)
linked_list.front(3)
linked_list.front(7)
linked_list.front(5)
linked_list.front(1)

linked_list.print_list()

#search
index=linked_list.search(7)
if index!=-1:
    print(f"Element 7 is found at index:{index}")
else:
    print("element not found")'''

#delete freater than 25
'''class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    #add at last
    def add(self,data):
        new_node=Node(data)
        if not self.head:
            self.head=new_node
        else:
            curr=self.head
            while curr.next:
                curr=curr.next
                curr.next=new_node
    #delete
    def delete_greater(self):
        curr=self.head
        prev=None
        while curr:
            if curr.data>25:
                if prev is None:
                    self.head=curr.next
                else:
                    prev.next=curr.next
            else:
                prev=curr
                curr=curr.next
            #print list
    def print_list(self):
        curr=self.head
        while curr:
            print(curr.data,end="->")
            curr=curr.next
        print("null")
linked_list=LinkedList()

n=int(input("enter elements:"))

for _ in range(n):
    number=int(input("enter a number:"))
    if 1<=number<=50:
        linked_list.add(number)
    else:
        print("please enter a number in the given range")
        continue

linked_list.print_list()

linked_list.delete_greater()
linked_list.print_list()'''

#using ollections
'''import collections
linked_list=collections.deque()

#add
linked_list.append("one")
linked_list.append("two")
linked_list.append("three")
print(linked_list)
#insert
linked_list.insert(0,"zero")
print(linked_list)
#delete last
linked_list.pop()
print(linked_list)
#delete particular
linked_list.remove('zero')
print(linked_list)'''

#reverse(recursively)
'''class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    def rev_list(head):
        if head is None or head.next is None:
            return head
        rest=Node.rev_list(head.next)
        head.next.next=head
        head.next=None
        return rest
head=Node(1)
head.next=Node(2)
head.next.next=Node(3)
head.next.next.next=Node(4)
head.next.next.next.next=Node(5)

rev_head=Node.rev_list(head)

curr=rev_head
while curr:
    print(curr.data,end="->")
    curr=curr.next
print("null")'''


#remove nth from end
'''class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
def remove_n(head,n):
    fast=head
    slow=head

    for _ in range(n):
        if fast is None:
            return head     #handle case where n is greater than list length
        fast=fast.next

#if fast reaches the end, remove head
    if fast is None:
        return head.next
#move fast and slow together to reach end
    while fast.next:
        fast=fast.next
        slow=slow.next

#remove the node pointed to by 'slow'
    slow.next=slow.next.next
    return head

head=Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

n=2

new_head=remove_n(head,n)

curr=new_head
while curr:
    print(curr.data,end="->")
    curr=curr.next
print("null")'''

#palindrome or not
'''class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
def is_palin(head):
    if head is None or head.next is None:
        return True

    slow=head
    fast=head
    while fast and fast.next:
        slow=slow.next
        fast=fast.next.next

    second_half=reverse_list(slow)
    first_half=head
    while second_half:
        if first_half.data!=second_half.data:
            return False
        first_half=first_half.next
        second_half=second_half.next
    reverse_list(slow)

    return True
def reverse_list(head):
    prev=None
    curr=head
    while curr:
        next_node=curr.next
        curr.next=prev
        prev=curr
        curr=next_node
    return prev
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(2)
head.next.next.next.next = Node(1)

if is_palin(head):
    print("palindrome")
else:
    print("not")'''

#detecting loop(cycle)

'''class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
def has_cycle(head):
slow=head
    fast=head
    while fast and fast.next:
        slow=slow.next
        fast=fast.next.next

        if slow==fast:
            return True

    return False
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = head  # Create a loop

if has_cycle(head):
    print("has a loop")
else:
    print("no loop")'''









