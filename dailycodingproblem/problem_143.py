"""
This problem was asked by Amazon.

Given a pivot x, and a list lst, partition the list into three parts.

The first part contains all elements in lst that are less than x
The second part contains all elements in lst that are equal to x
The third part contains all elements in lst that are larger than x
Ordering within a part can be arbitrary.

For example, given x = 10 and lst = [9, 12, 3, 5, 14, 10, 10], one partition may be [9, 3, 5, 10, 10, 12, 14].


Input: int, list of ints
Output: ??? (work w/ solution that mutates original array)


SOLUTION 1: time O(N) space(N)
i. create three arrays, one for less than, one for equal, and one for greater than
ii. iterate through the array, appending ints into appropriate array
iii. return less array + equal array + greater array


-> SOLUTION 2: time O(N) space(1)
i. initialize less and greater as the indices we will sent number (less = 0, greater = len(lst) - 1)
ii. iterate through the array
iii. if number is less than pivot, swap values at current index and index less, and increment less
iv. if number is greater than pivot, swap values at current index and index greater, and decrement greater
"""

class Solution:
    def partitionList(self, pivot: int, lst: list[int]):
        def _swap(x: int, y: int):
            (lst[x], lst[y]) = (lst[y], lst[x])
            return
        
        N = len(lst)
        less, greater, equal = 0, N - 1, -1

        for i in range(N):

            if lst[i] > pivot:
                while lst[i] > pivot:
                    _swap(less, i)
                    less += 1
                continue
            if lst[i] < pivot:
                while lst[i] < pivot:
                    _swap(greater, i)
                    greater -= 1
                continue
            if lst[i] == pivot and not equal:
                equal = i + 1
            elif lst[i] == pivot:
                _swap(equal, i)
                equal += 1
            
        # less, equal, greater = [], [], []
        
        # for num in lst:
        #     if num < pivot:
        #         less.append(num)
        #     elif num == pivot:
        #         equal.append(num)
        #     else:
        #         greater.append(num)

        # return less + equal + greater

solution = Solution()

lst1 = [9,12,3,5,14,10,10]
solution.partitionList(10, lst1) 
print(lst1) # -> ~[9, 3, 5, 10, 10, 12, 14]
lst2 = [3,8,2,5,1,4,5,7,6]
solution.partitionList(5, lst2) 
print(lst2) # -> ~[2, 1, 3, 4, 5, 5, 8, 7, 6]