/*

link to problem: https://leetcode.com/problems/longest-common-prefix/description/

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

*/

function longestCommonPrefix(strs: string[]): string {

    if (!strs.length) return "";

    let res: string = strs[0], arrayLength = strs.length;

    for (let i = 1; i < arrayLength && res.length; i++) {

        const current = strs[i];

        for (let j = 0; j < res.length; j++) {
            if (res[j] !== current[j]) {
                res = res.slice(0, j);
                break;
            }
        }

    }

    return res;

}

/*

First version of this function I sorted the array from biggest to smallest in order to use it as a queue




*/