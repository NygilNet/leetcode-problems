"""
This problem was asked by Google.

Given a sorted list of integers, square the elements and give the output in sorted order.

For example, given [-9, -2, 0, 2, 3], return [0, 4, 4, 9, 81].


input: sorted list of ints
output: sorted list of ints


FIRST, EASY O(n log n) solution
i. map each element to its square
ii. sorted mapped list
iii. return


O(n) solution w/ queue
i. create empty queue
ii. iterate over array
iii. if element is negative
    iv. store square in queue and remove current element from list
v. if element is positive
    vi. if first element is between current element and next element
        vii. popleft element from queue and add it back to the list
    viii. square element and update list


"""

from collections import deque
class Solution:
    def squareAndSortList(self, l: list[int]) -> list[int]:
        N = len(l)
        res = []
        stack = deque()

        for i in range(N):
            ele = l[i]
            square = ele ** 2
            if ele < 0:
                stack.appendleft(square)
            else:
                last_val = res[-1] if res else 0
                while stack and last_val <= stack[0] <= square:
                    res.append(stack.popleft())
                res.append(square)
        return res + list(stack)

# from collections import deque
# class Solution:
#     def squareAndSortList(self, l: list[int]) -> list[int]:
#         N = len(l)
#         res = []
#         queue = deque()

#         for i in range(N):
#             ele = l[i]
#             square = ele ** 2
#             if ele < 0:
#                 queue.append(square)
#             else:
#                 last_val = res[-1] if res else 0
#                 while queue and last_val <= queue[-1] <= square:
#                     res.append(queue.pop())
#                 res.append(square)
#         while queue:
#             res.append(queue.pop())
#         return res
    
solution = Solution()
print(solution.squareAndSortList([-9, -2, 0, 2, 3])) # -> [0, 4, 4, 9, 81]