# Write a Python program to search a specific item in a singly linked list and return true if the item is found otherwise return false.


class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def append_item(self, item):
        node = Node(item)
        if self.head:
            self.tail.next = node
            self.tail = node
        else:
            self.head = node
            self.tail = node

    def search_list(self, item):
        curr_item = self.head
        if curr_item.value == item:
            return True

        while curr_item.next:
            if curr_item.next.value == item:
                return True
            curr_item = curr_item.next

        return False


linked_list = LinkedList()
linked_list.append_item(1)
linked_list.append_item(2)
linked_list.append_item(3)

print(linked_list.search_list(1))
