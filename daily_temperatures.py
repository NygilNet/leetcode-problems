"""
link to problem: https://neetcode.io/problems/daily-temperatures


You are given an array of integers temperatures where temperatures[i] represents the daily temperatures on the ith day.

Return an array result where result[i] is the number of days after the ith day before a warmer temperature appears on a future day. If there is no day in the future where a warmer temperature will appear for the ith day, set result[i] to 0 instead.


Input: integer array
Output: integer array 



"""

def dailyTemperatures(temperatures: list[int]) -> list[int]:
        n = len(temperatures)
        for i in range(n):
            temp = temperatures[i]
            count = 1
            j = i + 1
            while j <= n:
                if j >= n:
                    temperatures[i] = 0
                    break
                if temp < temperatures[j]:
                    temperatures[i] = count
                    break
                count += 1
                j += 1
        return temperatures 