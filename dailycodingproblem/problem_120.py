"""
This problem was asked by Microsoft.

Implement the singleton pattern with a twist. First, instead of storing one instance, store two instances. And in every even call of getInstance(), return the first instance and in every odd call of getInstance(), return the second instance.
"""

class Solution:
    def getInstance(self, instance1, instance2):
        self.count = -1

        def _innerFunction():
            self.count += 1
            if self.count % 2 == 0:
                return instance1
            else:
                return instance2
            
        return _innerFunction

solution = Solution()
second_solution = Solution()
getInstance = solution.getInstance("instance a", "instance b")
getSecondInstance = second_solution.getInstance(12345, 54321)

print(getInstance()) # -> instance a
print(getSecondInstance()) # -> 12345
print(getInstance()) # -> instance b
print(getInstance()) # -> instance a
print(getSecondInstance()) # -> 54321
print(getInstance()) # -> instance b
print(getInstance()) # -> instance a
print(getSecondInstance()) # -> 12345

