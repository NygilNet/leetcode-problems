"""
The ancient Egyptians used to express fractions as a sum of several terms where each numerator is one. For example, 4 / 13 can be represented as 1 / 4 + 1 / 18 + 1 / 468.

Create an algorithm to turn an ordinary fraction a / b, where a < b, into an Egyptian fraction.


Input: ??
Output: ??


the example uses 1 / 4 as the first step in the Egyptian fraction since it's the closest fraction w/ 1 as the numerator that doesn't go over our target

we can get from 4 / 13 -> 1 / 4 by taking the reminder between 4/13 and making it the denominator of our first fraction


- create an array to store our fractions
...
- join the array into a string w/ " + " as the join
- return the string
"""

class Solution:
    def convertIntoEgyptianFraction(self, a: int, b: int) -> str:
        if not a < b:
            raise ValueError("numerator must be greater than the denominator")
        res = []
        target, running_total = a / b, 0

        while (running_total != target):
            fraction = "1 / "

            

            res.push(fraction)
        
        return " + ".join(res)
