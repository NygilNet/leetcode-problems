"""
This problem was asked by Google.

Given two rectangles on a 2D graph, return the area of their intersection. If the rectangles don't intersect, return 0.

For example, given the following rectangles:

{
    "top_left": (1, 4),
    "dimensions": (3, 3) # width, height
}
and

{
    "top_left": (0, 5),
    "dimensions": (4, 3) # width, height
}
return 6.


Input: two dictionaries 
Output: int


I. find the intersections
    i. points of the rectangle are top

II. return the area

"""
class Rectangle:
    def __init__(self, top_left, dimensions) -> None:
        (dx, dy) = dimensions
        self.top_left = top_left
        (x, y) = top_left
        self.top_right = (x + dx, y)
        self.bottom_left = (x, y - dy)
        self.bottom_right = (x + dx, y - dy)
    

    @property
    def bottom(self):
        return self.bottom_left(1)
    

    @property
    def top(self):
        return self.top_left(1)
    

    @property
    def left(self):
        return self.top_left(0)
    

    @property
    def right(self):
        return self.top_right(0)
    

    @property
    def area(self) -> int:
        return (self.right - self.left) * (self.top - self.bottom)

class Solution:
    def areaOfIntersection(self, rect1, rect2) -> int:
        RECT1, RECT2 = Rectangle(rect1.top_left, rect1.dimensions), Rectangle(rect2.top_left, rect2.dimensions)

        res_top_left, res_dimensions = (None, None), (0, 0)

        for i in range(max(RECT1.top, RECT2.top), min(RECT1.bottom, RECT2.bottom), - 1):
            if not res_top_left[1] and ((RECT1.bottom <= i <= RECT1.top) and (RECT2.bottom <= i <= RECT2.top)):
                res_top_left[1] = i
            elif res_top_left[1] and ((RECT1.bottom <= i <= RECT1.top) and (RECT2.bottom <= i <= RECT2.top)):
                res_dimensions[1] += 1
            else:
                break

        for j in range(min(RECT1.left, RECT2.left), max(RECT1.right, RECT2.right)):
            if not res_top_left[0] and ((RECT1.left <= j <= RECT1.right) and (RECT2.left <= j <= RECT2.right)):
                res_top_left[0] = j
            elif res_top_left[0] and ((RECT1.left <= j <= RECT1.right) and (RECT2.left <= j <= RECT2.right)):
                res_dimensions[0] += 1
            else:
                break
        
        if not res_top_left[0] and res_top_left[1]:
            return 0
        
        res = Rectangle(res_top_left, res_dimensions)
        return res.area
    

solution = Solution()
r1 = {
    'top_left': (1, 4),
    'dimensions': (3, 3)
}

r2 = {
    'top_left': (0, 5),
    'dimensions': (4, 3)
}
print(solution.areaOfIntersection(r1, r2)) # -> 6
