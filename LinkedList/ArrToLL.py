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
        print("->".join(map(str,elements)))

    def LLappend(self, x):
        newnode = LLnode(x)
        
        if self.head is None:
            self.head = newnode
            return

        current = self.head
        while current.next:
            current = current.next

        current.next = newnode


def array_to_linked_list():
    input_array = input("Enter the elements of the array separated by spaces: ").split()
    ll = LL()
    for element in input_array:
        ll.LLappend(int(element))
    return ll


ll = array_to_linked_list()
ll.display()
