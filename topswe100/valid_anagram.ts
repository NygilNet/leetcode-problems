/*

link to problem: https://leetcode.com/problems/valid-anagram/description/

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.



*/

function isAnagram(s: string, t: string): boolean {

    const map = new Map();

    for (let letter of s) {
        map.set(letter, (map.get(letter) || 0) + 1 );
    }

    for (let letter of t) {
        if (!map.has(letter)) return false;
        map.set(letter, map.get(letter) - 1);
    }

    return [...map.values()].filter(Boolean).length === 0;

}