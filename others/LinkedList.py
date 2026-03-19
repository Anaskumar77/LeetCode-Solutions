#singly linked list 

class Node:
    def __init__(self,val,next= None):
        self.value = val
        self.next = next

    def __str__(self):
        return str(self.value)
    

Head = Node(1)
A = Node(3)
B = Node(7)
C = Node(9)

Head.next = A
A.next = B
B.next = C
C.next = None

# Traverse the list - 0(n)

curr = Head

while curr:
    print(curr)
    curr = curr.next 

# displaying linked list 

def display(Node):
    curr = Node
    list = []

    while curr:
        list.append(str(curr.value))
        curr = curr.next

    print(' -> '.join(list))

display(Head)


# search for node value 

def search(Head, value):
    curr = Head
    while curr:
        if curr.value == value:
            return True
        curr = curr.next
    return False

print(search(Head,10))
print(search(Head,9))
