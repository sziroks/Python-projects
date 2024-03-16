# Write a Python program to access a specific item in a singly linked list using index value.


class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.length = 0

    def append_item(self, item):
        node = Node(item)
        if self.head:
            self.tail.next = node
            self.tail = node
        else:
            self.head = node
            self.tail = node

        self.length += 1

    def __getitem__(self, node_index):
        if self.head:
            if node_index <= self.length - 1:
                curr_node = self.head
                for _ in range(0, node_index):
                    curr_node = curr_node.next
                return curr_node.value
            else:
                return f"Node index out of range <0, {self.length - 1}>"
        else:
            return "Empty linked list"


llist = LinkedList()
# llist.append_item(1)
# llist.append_item(2)
# llist.append_item(3)

print(llist[2])
