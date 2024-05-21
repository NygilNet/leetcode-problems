"""
link to problem: https://leetcode.com/problems/assign-cookies

"""

def findContentChildren(self, g: List[int], s: List[int]) -> int:
    # sort children and cookies
    res = 0
    g.sort(reverse=True)
    s.sort(reverse=True)
    while g and s:
        child = g.pop()
        cookie = s.pop()
        while s and cookie < child:
            cookie = s.pop()
        if cookie >= child: res += 1
    return res