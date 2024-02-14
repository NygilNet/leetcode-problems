/*

link to leetcode: https://leetcode.com/problems/longest-palindromic-substring/description/

Given a string s, return the longest 
palindromic substring in s.

*/

function longestPalindrome(s: string): string {
    const lengthOfS = s.length;
    if (lengthOfS === 0) return "";

    function _expandAroundCenter(s: string, left: number, right: number): number {
        while (left >= 0 && right < s.length && s[left] === s[right]) {
            left--;
            right++;
        }
        return right - left - 1;
    }

    let start = 0, end = 0;

    for (let i = 0; i < lengthOfS; i++) {
        const len1 = _expandAroundCenter(s, i, i);
        const len2 = _expandAroundCenter(s, i, i + 1);
        const len = Math.max(len1, len2);
        if (len > end - start) {
            start = i - Math.floor((len - 1) / 2);
            end = i + Math.floor(len / 2);
        }
    }

    return s.slice(start, end + 1);
}

/*
function longestPalindrome(s: string): string {
    let longest = "";

    function _isPalindrome(str: string): boolean {
        for (let i = 0; i < Math.floor(str.length / 2); i++) {
            if (str[i] !== str[str.length - (1 + i)]) return false;
        }
        return true;
    }

    function _generateAllSubStrings(index: number, str: string = "") {
        if (index > s.length - 1) return;
        str += s[index];

        if (_isPalindrome(str) && str.length > longest.length) longest = str;

        _generateAllSubStrings(index + 1);
        _generateAllSubStrings(index + 1, str);
    }

    _generateAllSubStrings(0);

    return longest;
};
*/