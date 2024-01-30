/*

Write a function that takes in a string and that returns its longest substring without duplicate characters. Assume that there will only be one longest substring without duplication.


initialize a map to track each character
iterate through the string, generating x number of substrings w/o repeating character
determine which substring is the longest
return a substring

abbac

recersive function

for each character in the string call recursive function
if last letter of string called equals the current letter, check if string is longest and return
else add character to the string and call recursive function on next letter if it exists


*/


function longestSubstring(str) { 

    let longest = "", set = new Set(), current = "";

    for (
        let i = 0, j = 1;
        i < str.length;
        i++, j++
    ) {
        set.add(str[i]);
        current += str[i];
        if (set.has(str[j]) || !str[j]) {
            longest = current.length > longest.length ? current : longest;
            current = "";
            set.clear();
        }
    }

    return longest;

}

console.log(longestSubstring('abbac')); // bac
console.log(longestSubstring("bacaa")); // bac
console.log(longestSubstring("b")); // b

/*

According to ChatGPT:

    Time complexity: O(n)
    Space complexity: O(min(n, m)) where n is the length of the string and m is the length of the character set


Previous versions of function:

    // let longest = ""

    // function _recurse(currentString, currentSet, i) {
    //     if (currentSet.has(str[i]) || !str[i]) {
    //         longest = currentString.length > longest.length ? currentString : longest;
    //         return;
    //     }

    //     currentString += str[i++];

    //     _recurse(currentString, currentSet, i);
        

    // }

    // for (let i = 0; i < str.length; i++) {
    //     let s = str[i];
    //     _recurse(s, new Set([s]), i + 1);
    // }

    // return longest;

function works but with bad time and space

//    const alphabet = 'abcdefghijklmnopqrstuvwxyz';

//    function _generateEmptyMap() {
//         let m = {};
//         for (let letter of alphabet) {
//              m[letter] = 0;
//         }
//         return m;
//    }

//    let map = _generateEmptyMap();

//    let startIndex = 0, longest = "";

//    for (let i = 0; i < str.length; i++) {
//         if (!map[str[i]]) {
//             map[str[i]]++;
//             continue;
//         }
//         let currentString = str.slice(startIndex, i);
//         longest = currentString.length > longest.length ? currentString : longest;
//         map = _generateEmptyMap();
//         startIndex = i;
//    }

//    return longest;

solution did not work and alot of unnecessary space used with the generate empty map helper function

*/