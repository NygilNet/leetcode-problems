"""

This problem was asked by Apple.

Suppose you have a multiplication table that is N by N. That is, a 2D array where the value at the i-th row and j-th column is (i + 1) * (j + 1) (if 0-indexed) or i * j (if 1-indexed).

Given integers N and X, write a function that returns the number of times X appears as a value in an N by N multiplication table.

For example, given N = 6 and X = 12, you should return 4, since the multiplication table looks like this:

| 1 | 2 | 3 | 4 | 5 | 6 |

| 2 | 4 | 6 | 8 | 10 | 12 |

| 3 | 6 | 9 | 12 | 15 | 18 |

| 4 | 8 | 12 | 16 | 20 | 24 |

| 5 | 10 | 15 | 20 | 25 | 30 |

| 6 | 12 | 18 | 24 | 30 | 36 |

And there are 4 12's in the table.

input: N (the size of the multiplication table), X (the value we are looking for in the table)
output: int (the number of time X appears in the multiplication table)


METHOD 1: memoization

i. generate a N * N 2D array
ii. define a function that either returns a value if it already exists in the matrix or recursively calculates the product of the two numbers
    iii. if it is the first time we are calculating the number and it equals X increment a count
iv. call helper function
v. return the count

"""

def timesValueAppearsInTable(N: int, X: int) -> int:
    multi_table = []
    
    for _ in range(N + 1):
        row = []
        for _ in range(N + 1):
            row.append(0)
        multi_table.append(row)
        
    count = 0

    def _multiply(a: int, b: int) -> int:
        if b == 0 or a == 0:
            return 0
        if b == 1:
            return a
        if multi_table[a][b] or multi_table[b][a]:
            return multi_table[a][b] or multi_table[b][a]
       
        nonlocal count
        product = a + _multiply(a, b - 1)
        
    
        multi_table[a][b] = product
        multi_table[b][a] = product
        count += 2

        return product
           
    for i in range(N + 1):
        _multiply(i, N)

    return count