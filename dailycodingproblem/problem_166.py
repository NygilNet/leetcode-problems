"""
This problem was asked by Uber.

Implement a 2D iterator class. It will be initialized with an array of arrays, and should implement the following methods:

next(): returns the next element in the array of arrays. If there are no more elements, raise an exception.
has_next(): returns whether or not the iterator still has elements left.
For example, given the input [[1, 2], [3], [], [4, 5, 6]], calling next() repeatedly should output 1, 2, 3, 4, 5, 6.

Do not use flatten or otherwise clone the arrays. Some of the arrays can be empty.

"""

class twoDIterator:
    def __init__(self, twod) -> None:
        self._twod = twod
        self._R = len(twod)
        self.row, self.col = 0, 0

    def next(self):
        """
        returns the next element in the array of arrays.
        if there are no more elements, raise an exception
        """
        while not ((0 <= self.row < self._R) and (0 <= self.col < len(self._twod[self.row]))): 
            if self.row == self._R and self.col == len(self._twod[self._R - 2]):
                raise StopIteration("There are no more elements in the iterator")
            
            self.col += 1
            if self.col >= len(self._twod[self.row]):
                self.col = 0
                self.row += 1
        
        element = self._twod[self.row][self.col]
        self.col += 1
        return element


    def has_next(self) -> bool:
        """
        returns whether or not the iterator still has elements left
        """
        return self. row < self._R and self.col < len(self._twod[self.row])

test = twoDIterator([[1, 2], [3], [], [4, 5, 6]])
print(test.has_next()) # -> True
print(test.next()) # -> 1
print(test.next()) # -> 2
print(test.next()) # -> 3
print(test.next()) # -> 4
print(test.next()) # -> 5
print(test.next()) # -> 6
print(test.has_next()) # -> False
print(test.next()) # -> raise an exception