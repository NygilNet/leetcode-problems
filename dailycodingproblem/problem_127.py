"""
This problem was asked by Microsoft.

Let's represent an integer in a linked list format by having each node represent a digit in the number. The nodes make up the number in reversed order.

For example, the following linked list:

1 -> 2 -> 3 -> 4 -> 5
is the number 54321.

Given two linked lists in this format, return their sum in the same linked list format.

For example, given

9 -> 9
5 -> 2
return 124 (99 + 25) as:

4 -> 2 -> 1
"""
class LinkedListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next


class Solution:
    def sumOfTwoLinkedListAsLinkedList(self, list1: LinkedListNode, list2: LinkedListNode) -> LinkedListNode:
        first_pointer, second_pointer = list1, list2
        first_num, second_num = '', ''

        while first_pointer or second_pointer:
            if first_pointer:
                first_num = str(first_pointer.val) + first_num
                first_pointer = first_pointer.next
            if second_pointer:
                second_num = str(second_pointer.val) + second_num
                second_pointer = second_pointer.next

        first_num = int(first_num)
        second_num = int(second_num)

        res = str(first_num + second_num)
        prev = None

        for i in range(len(res)):
            current_node = LinkedListNode(int(res[i]), prev)
            prev = current_node

        return prev
    
solution = Solution()
lst1 = LinkedListNode(9, LinkedListNode(9))
lst2 = LinkedListNode(5, LinkedListNode(2))
res = solution.sumOfTwoLinkedListAsLinkedList(lst1, lst2)

print(res.val, res.next.val, res.next.next.val) # -> 4 -> 2 -> 1