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

    def LLappend(self, x):
        newnode = LLnode(x)
        
        if self.head is None:
            self.head = newnode
            return

        current = self.head
        while current.next:
            current = current.next

        current.next = newnode

def addTwoNumbers(l1, l2):
    dummy = LLnode()
    cun = dummy
    carry = 0
    while l1 or l2 or carry:
        v1 = l1.data if l1 else 0
        v2 = l2.data if l2 else 0
        val = v1 + v2 + carry
        carry = val // 10
        val = val % 10
        cun.next = LLnode(val)
        cun = cun.next
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
    return(dummy.next)

def array_to_linked_list():
    input_array1 = input("Enter the elements of the array separated by spaces for L1: ").split()
    l1 = LL()
    for element in input_array1:
        l1.LLappend(int(element))

    input_array2 = input("Enter the elements of the array separated by spaces for L2: ").split()
    l2 = LL()
    for element in input_array2:
        l2.LLappend(int(element))
    
    result = addTwoNumbers(l1.head,l2.head)
    result_ll = LL()
    result_ll.head = result
    return result_ll

l = array_to_linked_list()
l.display()
