"""
This problem was asked by Epic.

The "look and say" sequence is defined as follows: beginning with the term 1, each subsequent term visually describes the digits appearing in the previous term. The first few terms are as follows:

1
11
21
1211
111221
As an example, the fourth term is 1211, since the third term consists of one 2 and one 1.

Given an integer N, print the Nth term of this sequence.
"""

class Solution:
    def lookAndSay(self, N: int):
        if N <= 0 or N is not int(N):
            raise ValueError('N must be a positive integer')
        term = "1"
        if N == 1:
            print(term)

        for _ in range(1, N):
            previous_term = term
            digit, count = 0, 0
            term = ""

            for d in previous_term:
                if digit == 0:
                    digit = d
                if d != digit:
                    term += f"{count}{digit}"
                    digit = d
                    count = 0
                count += 1
            
            
        print(term)