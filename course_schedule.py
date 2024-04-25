"""

link to leetcode: https://leetcode.com/problems/course-schedule/description/

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.

"""
from collections import deque

def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    adjacency_list = defaultdict(list)

    for course, prerequisite in prerequisites:
        adjacency_list[course].append(prerequisite)

    visited = set()

    def _has_cycle(course: int, visited: set) -> bool:
        # success base case
        if len(adjacency_list[course]) == 0:
            return False
        # fail base case
        if course in visited:
            return True

        visited.add(course)

        for last_course in adjacency_list[course]:
            if _has_cycle(last_course, visited.copy()):
                return True
        
        adjacency_list[course] = []
        
    for course in range(numCourses):
        if _has_cycle(course, set()):
            return False

    return True