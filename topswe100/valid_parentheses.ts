/*

link to problem: https://leetcode.com/problems/valid-parentheses/description/

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

*/

function isValid(s: string): boolean {
    if (s.length % 2 !== 0) return false;

    const openBrackets = new Set(["(", "{", "["]);
    const sameOpenBracket = {
        ")": "(",
        "}": "{",
        "]": "["
    }
    const stack: string[] = [];

    for (const character of s) {
        const isOpen = openBrackets.has(character);
        if (isOpen) {
            stack.push(character);
        } else {
            const compliment = sameOpenBracket[character];
            const lastOpen = stack.pop();
            if (compliment !== lastOpen) return false;
        }
    }

    return stack.length === 0;
};

// function isValid(s: string): boolean {
    
//     function _isOpenBracket(c: string): boolean {
//         return c === "(" || c === "{" || c === "[";
//     }

//     function _sameOpenBracket(c: string): string {
//         switch (c) {
//             case ")":
//                 return "(";
//             case "}":
//                 return "{";
//             case "]":
//                 return "[";
//             default:
//                 return "";
//         }
//     }

//     const stack: string[] = [];

//     for (const character of s) {
//         const isOpen = _isOpenBracket(character);
//         if (isOpen) {
//             stack.push(character);
//         } else {
//             const compliment = _sameOpenBracket(character);
//             const lastOpen = stack.pop();
//             if (compliment !== lastOpen) return false;
//         }
//     }

//     return stack.length === 0;
// };

// function isValid(s: string): boolean {

//     function _isOpenBracket(c: string): boolean {
//         return c === "(" || c === "{" || c === "[";
//     }

//     function _sameOpenBracket(c: string): string {
//         switch (c) {
//             case ")":
//                 return "(";
//             case "}":
//                 return "{";
//             case "]":
//                 return "]";
//             default:
//                 return "";
//         }
//     }

//     const tracking = {
//         "(" : false,
//         ")": false,
//         "{": false,
//         "}": false,
//         "[": false,
//         "]": false
//     }

//     for (const character of s) {
//         const isOpen = _isOpenBracket(character);
//         if (isOpen) {
//             if (tracking[character]) return false;
//             tracking[character] = true;
//         } else {
//             const compliment = _sameOpenBracket(character);
//             if (tracking[character] || !tracking[compliment]) return false;
//             tracking[character] = false;
//             tracking[compliment] = false;
//         }
//     }

//     return !tracking["("] && !tracking["{"] && !tracking["["]; 
// }