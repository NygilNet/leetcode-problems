/*

link to problem: https://leetcode.com/problems/group-anagrams/description/

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
 

Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.

Input: array of strings (will always have at least one string)
Output: array of arrays (groups that are the same anagram)

looking of output of examples, we can use a stack to go through the array

design an object that tracks 

*/


function groupAnagrams(strs: string[]): string[][] {
    const groupOfAnagrams: Map<string, string[]> = new Map();

    while (strs.length) {
        const str = strs.pop()!;
        const sortedStr = str.split("").sort().join("");
        const values: string[] = groupOfAnagrams.get(sortedStr) || [];

        groupOfAnagrams.set(sortedStr, values.concat(str));
    }

    const res: string[][] = [];
    for (const [_, value] of groupOfAnagrams) {
        res.push(value);
    }

    return res;
};

// const groupOfAnagrams: Array<[Map<string, number>, string[]]> = [];
// let empty = false;

// while (strs.length) {
//     const str = strs.pop()!;
//     if (str === "") {
//         if (!empty) {
//             const emptyMap = new Map();
//             emptyMap.set("_", 1);
//             groupOfAnagrams.push([emptyMap, [""]]);
//             empty = true;
//         }
//         continue;
//     }
//     let added = false;
//     for (const [object, group] of groupOfAnagrams) {
//         const clone = {...object};
//         for (const char of str) {
//             if (clone[char] === undefined || clone[char] === 0) break;
//             clone[char]--;
//         }
//         const checkIfSameAnagram = Object.values(clone).filter(n => n !== 0);
//         if (checkIfSameAnagram.length < 1) {
//             group.push(str);
//             added = true;
//             break;
//         }
//     }
//     if (!added) {
//         const o = new Map();
//         for (const c of str) {
//             o[c] = o[c] || 0;
//             o[c]++;
//         } 
//         groupOfAnagrams.push([o, [str]]);
//     }
// }

// return groupOfAnagrams.map(group => group[1]); 