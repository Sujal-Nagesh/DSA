class LLnode:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LL:
    def __init__(self):
        self.head = None

    def display(self):
        if self.head is None:
            print("Linked list is empty")
            return

        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        print(elements)

    def LLappend(self,x):
        
        newnode = LLnode(x)
        
        if self.head == None:
            self.head = newnode
            return

        current = self.head
        while current.next:

            current = current.next

        current.next = newnode

    def InsertNodeAtPosition(self,data,position):

        if position < 0:
            print("Invalid position")
            return

        new_node = LLnode(data)

        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head
        for i in range(position - 1):
            if current is None:
                print("Position out of range")
                return
            current = current.next

        if current is None:
            print("Position out of range")
            return

        new_node.next = current.next
        current.next = new_node


def array_to_linked_list():
    input_array = input("Enter the elements of the array separated by spaces : ").split()
    ll = LL()
    for element in input_array:
        ll.LLappend(int(element))
    return ll


ll = array_to_linked_list()

ll.display()

x = int(input("enter the input data : "))
y = int(input("Enter the position : "))

ll.InsertNodeAtPosition(x,y)

ll.display()
