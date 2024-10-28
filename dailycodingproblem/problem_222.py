"""
This problem was asked by Quora.

Given an absolute pathname that may have . or .. as part of it, return the shortest standardized path.

For example, given "/usr/bin/../bin/./scripts/../", return "/usr/bin/".

also link to leetcode: https://leetcode.com/problems/simplify-path/


Input: string (valid Unix path)
Output: the simplified Unix path



"""

class Solution:
    def simplifyPath(self, path: str) -> str:
        simplified_path = []
        all_actions = path.split("/")
        
        for action in all_actions:
            if action == "." or not action:
                continue
            elif action == "..":
                if simplified_path:
                    simplified_path.pop()
            else:
                simplified_path.append(action)

        return "/" + "/".join(simplified_path)

# from collections import deque
# class Solution:
#     def simplifyPath(self, path: str) -> str:
#         all_actions = path.split("/")
#         if not all_actions[-1]:
#             all_actions.pop()
#         queue = deque(all_actions)
#         simplified_path = []
#         simplified_path.append(queue.popleft())
#         root = queue.popleft()

#         if root == ".." or root == ".":
#             return "/"
#         simplified_path.append(root)

#         while queue:
#             current_action = queue.popleft()
#             if current_action == ".":
#                 continue
#             if current_action == "..":
#                 simplified_path.pop()
#             else:
#                 simplified_path.append(current_action)

#         return "/".join(simplified_path)

solution = Solution()
print(solution.simplifyPath("/home/"))
print(solution.simplifyPath("/home/user/Documents/../Pictures"))
print(solution.simplifyPath("/usr/bin/../bin/./scripts/../"))
