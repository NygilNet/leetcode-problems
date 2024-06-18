"""
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

For example, given [100, 4, 200, 1, 3, 2], the longest consecutive element sequence is [1, 2, 3, 4]. Return its length: 4.

Your algorithm should run in O(n) complexity.


Input: unsorted int array
Output: int

CAN NOT:
 - sort the array (O (n log n))

"""

class DoubledEndedListNode:
    def __init__(self, val: int) -> None:
        self.val = val
        self.next = None
        self.prev = None

class DoubledEndedList:
    def __init__(self, node: DoubledEndedListNode) -> None:
        self.head = node
        self.tail = node
        self.length = 1

def _addToHead(main: DoubledEndedList, toAdd: DoubledEndedList) -> bool:
    if toAdd.tail.val is not main.head.val - 1:
        return False
        
    toAdd.tail.next = main.head
    main.head = toAdd.head
    toAdd.tail = main.tail

    new_length = main.length + toAdd.length
    toAdd.length = new_length 
    main.length = new_length

    return True
    
def _addToTail(main: DoubledEndedList, toAdd: DoubledEndedList) -> bool:
    if toAdd.head.val is not main.head.val + 1:
        return False
        
    toAdd.head.prev = main.tail
    main.tail = toAdd.tail
    toAdd.head = main.head
    
    new_length = main.length + toAdd.length
    toAdd.length = new_length 
    main.length = new_length

    return True
        
        

class Solution:
    def longestConsecutiveSequenceInUnsortedArray(arr: list[int]) -> int:
        visited = {}

        for ele in arr:
            if ele not in visited:
                node = DoubledEndedListNode(ele)
                double_ended_list = DoubledEndedList(node)

                if ele + 1 in visited:
                    _addToTail(double_ended_list, visited[ele + 1])
                if ele - 1 in visited:
                    _addToHead(double_ended_list, visited[ele - 1])

                visited[ele] = double_ended_list

        return max([visited[v].length for v in visited])
    
print(Solution.longestConsecutiveSequenceInUnsortedArray([100, 4, 200, 1, 3, 2, 0, -1]))