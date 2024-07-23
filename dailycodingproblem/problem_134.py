"""
This problem was asked by Facebook.

You have a large array with most of the elements as zero.

Use a more space-efficient data structure, SparseArray, that implements the same interface:

init(arr, size): initialize with the original large array and size.
set(i, val): updates index at i with val.
get(i): gets the value at index i.
"""

from collections import defaultdict
class SparseArray:
    def __init__(self, arr: list[int], size: int) -> None:
        self.d = defaultdict(int)
        for i, ele in enumerate(arr):
            if ele != 0:
                self.d[i] = ele
        self.size = size


    def set(self, i: int, val: int) -> bool:
        if i > self.size:
            raise IndexError("Index is out of bounds.")
        self.d[i] = val
        return True


    def get(self, i: int) -> int:
        if i > self.size:
            raise IndexError('Index is out of bounds.')
        return self.d[i]