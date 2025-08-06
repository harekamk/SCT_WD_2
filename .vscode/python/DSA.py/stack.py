# stack1=[]

# stack1.append(10)
# stack1.append(20)
# stack1.append(30)

# print(stack1)   

# item=stack1.pop()

# print(item)
# print(stack1) 

# (peek)top=stack1[-1]
# print(top)


# using arraylist or collections framework
'''class Stack:
    def __init__(self):
        self.stack=[]

    def push(self,item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()
    
    def is_empty(self):
        return len(self.stack)==0
    
    def size(self):
        return len(self.stack)
    
    def peek(self):
        return self.stack[-1]
    
stack1=Stack()

stack1.push(10)
stack1.push(20)
stack1.push(30)

print("top item=",stack1.peek())

print("popped item=",stack1.pop())
print("next popped item=",stack1.pop())

print("is it empty?",stack1.is_empty())

print("size=",stack1.size())'''

# using linked list

'''class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Stack:
    def __init__(self):
        self.top=None

    def push(self,item):
        new_node=Node(item)
        new_node.next=self.top
        self.top=new_node

    def pop(self):
        popped_node=self.top
        self.top=self.top.next
        return popped_node.data
    
    def peek(self):
        return self.top.data
    
    def is_empty(self):
        return self.top is None
    
    def size(self):
        curr=self.top
        count=0
        while curr:
            count+=1
            curr=curr.next
        return count
    
stack1=Stack()

stack1.push(10)
stack1.push(20)
stack1.push(30)
stack1.push(40)

print("top item=",stack1.peek())

print("popped item=",stack1.pop())

print("is empty?",stack1.is_empty())

print("size=",stack1.size())'''

#





















