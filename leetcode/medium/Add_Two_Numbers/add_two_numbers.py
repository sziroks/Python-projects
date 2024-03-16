from typing import Optional


class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, val=0):
        self.next = None
        self.head = None

    def append_node(self, value):
        node = Node(value)
        if self.head:
            self.tail.next = node
            self.tail = node
        else:
            self.head = node
            self.tail = node

    def print_list(self):
        curr_node = self.head
        while curr_node:
            print(curr_node.value)
            curr_node = curr_node.next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[LinkedList], l2: Optional[LinkedList]
    ) -> Optional[LinkedList]:
        reversed_list1 = []
        reversed_list2 = []

        l1_node = l1.head
        l2_node = l2.head

        while l1_node:
            reversed_list1.append(str(l1_node.value))
            l1_node = l1_node.next

        while l2_node:
            reversed_list2.append(str(l2_node.value))
            l2_node = l2_node.next

        num1 = int("".join(reversed(reversed_list1)))
        num2 = int("".join(reversed(reversed_list2)))

        result = str(num1 + num2)
        result_llist = LinkedList()
        for num in result:
            result_llist.append_node(num)

        return result_llist


llist1 = LinkedList()
llist1.append_node(0)
llist1.append_node(1)
llist1.append_node(2)


llist2 = LinkedList()
llist2.append_node(3)
llist2.append_node(4)
llist2.append_node(5)


solution = Solution()
print(solution.addTwoNumbers(llist1, llist2))
