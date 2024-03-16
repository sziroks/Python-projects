# Write a Python program to find the size of a singly linked list.


class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def print_list(self):
        if self.head:
            temp = self.head
            while temp:
                print(temp.value)
                temp = temp.next
        else:
            print("Linked list is empty")

    def append_item(self, item):
        node = Node(item)
        if self.tail:
            self.tail.next = node
            self.tail = node
        else:
            self.tail = node
            self.head = node

    def get_size(self):
        size = 0
        if self.head:
            size += 1
            curr_node = self.head
            while curr_node.next:
                size += 1
                curr_node = curr_node.next
        return size


class Node:
    def __init__(self, key) -> None:
        self.next = None
        self.value = key


llist = LinkedList()
llist.append_item(1)
llist.append_item(2)
llist.append_item(3)
llist.append_item("abc")

llist.print_list()
print(llist.get_size())
