class LLnode:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Solution:
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


    def deleteDuplicates(self):
        if self.head is None:
            return None
        
        temp = self.head
        while temp and temp.next is not None:
            if temp.data == temp.next.data:
                temp.next = temp.next.next
            else:
                temp = temp.next
        
        return self.head

def array_to_linked_list():
    input_array = input("Enter the elements of the array separated by spaces: ").split()
    input_array.sort()
    ll = Solution()
    for element in input_array:
        ll.LLappend(int(element))
    return ll

Ll = array_to_linked_list()
print("Original Linked List:")
Ll.display()


print("Linked List after removing duplicates:")
new_head = Ll.deleteDuplicates()
if new_head:
    Ll.head = new_head
    Ll.display()
else:
    print("Linked list is empty after removing duplicates")
