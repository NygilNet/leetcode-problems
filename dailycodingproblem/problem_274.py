"""
This problem was asked by Facebook.

Given a string consisting of parentheses, single digits, and positive and negative signs, convert the string into a mathematical expression to obtain the answer.

Don't use eval or a similar built-in parser.

For example, given '-1 + (2 + 3)', you should return 4.


Input: string
Output: int (or float??)

each step will use a stack so we can ensure that steps are done in the right order (i.e (5 + (1 + 4)) -> (5 + 5) -> 10)
PEMDAS
- find '(' for parentheses
- ignore exponent step
- find 'x' and/or '/' for multiplication and division
- find '+' and/or '-' for addition and subtraction 
"""

from collections import deque
class Solution:
    def evaluateString(self, s: str):
        total = 0
        parentheses_stack = deque()

        multiplication_division_stack = deque()

        addition_subtraction_stack = deque()

        return total
