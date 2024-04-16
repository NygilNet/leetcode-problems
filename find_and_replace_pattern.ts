/*

link to leetcode: https://leetcode.com/problems/find-and-replace-pattern/

Given a list of strings words and a string pattern, return a list of words[i] that match pattern. You may return the answer in any order.

A word matches the pattern if there exists a permutation of letters p so that after replacing every letter x in the pattern with p(x), we get the desired word.

Recall that a permutation of letters is a bijection from letters to letters: every letter maps to another letter, and no two letters map to the same letter.

*/

function findAndReplacePattern(words: string[], pattern: string): string[] {
    function _matchPattern(word: string): boolean {
        const permutation: Map<string,string> = new Map();
        const used: Set<string> = new Set();

        for (const letter of pattern) {
            if (!permutation.has(letter)) {
                permutation.set(letter, "");
            }
        }

        for (let i = 0; i < word.length; i++) {
            const letter = word[i];
            const charToMatch = pattern[i];
            const p = permutation.get(charToMatch);

            if (p && p !== letter) {
                return false;
            }

            if (!p) {
                if (!used.has(letter)) {
                    permutation.set(charToMatch, letter);
                    used.add(letter);
                } else {
                    return false;
                }
            }
        }

        return true;
    }


    return words.filter((word) => _matchPattern(word));
}