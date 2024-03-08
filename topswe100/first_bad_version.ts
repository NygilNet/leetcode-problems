/*

link to problem: https://leetcode.com/problems/first-bad-version/description/

You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

 

Example 1:

Input: n = 5, bad = 4
Output: 4
Explanation:
call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true
Then 4 is the first bad version.
Example 2:

Input: n = 1, bad = 1
Output: 1
 

Constraints:

1 <= bad <= n <= 231 - 1

It looks we need to perform a binary search in order to find the first bad version

i. define left pointer at 1 and right pointer at n
ii. while left less than or equal to right
    iii. calculate the mid point between left and right
    iv. if isBadVersion(mid) is false, update pointer to check later versions
    v. if isBadVersion(mid) is true,
        vi. if isBadVersion(mid - 1) is true, we have not found the easier bad version and have to update pointers to check earlier versions
        vii. if isBadVersion(mid - 1) is false, we have found the bad version and return mid

*/

var solution = function(isBadVersion: any) {

    return function(n: number): number {
        let left = 1, right = n;
        while (left < right) {
            const mid = left + Math.floor((right - left) / 2);
            if (isBadVersion(mid)) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        return left;
    }
}

/*

let left = 1, right = n;
while (left <= right) {
    const mid = left + Math.floor((right - left) / 2);
    if (isBadVersion(mid)) {
        if (isBadVersion(mid - 1)) {
            right = mid - 1;
        } else {
            return mid;
        }
    } else {
        left = mid + 1;
    }
}

*/