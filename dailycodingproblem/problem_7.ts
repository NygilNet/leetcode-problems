/*

This problem was asked by Facebook.

Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed.

Input: string (message containing numbers)
Output: number (number of ways the the message can be decoded)

METHOD 1: find every possible combination -> BACKTRACKING

i. initialize count variable @ 0

ii. define backtracking function

    iii. BASE CASE: reached the end of the string

        iv. increment count and return

    v. if current 1 - 2 digit is inbounds of 1 to 26

        vi. if there is more than 1 character left in string, call backtracking on next character

        vii. if there is more than 2 characters left in string, call backtracking on the next 2 characters

viii. call backtracking on using first character & first two characters

ix. return count


*/

function numberWaysToDecode(message: string): number {
    const codes: Set<string> = new Set();
    const alphabet = "_abcdefghijklmnopqrstuvwxyz";

    function _backtracking(queue: string, code: string): void {
        if (!queue.length) {
            codes.add(code);
            return;
        }

       const singleDigit = +queue[0];
       if (0 <= singleDigit && singleDigit <= 26) {
            _backtracking(queue.slice(1), code + alphabet[singleDigit]);
       }

       if (queue.length >= 2) {
            const doubleDigit = +(queue[0] + queue[1]);
            if (0 <= doubleDigit && doubleDigit <= 26) {
                _backtracking(queue.slice(2), code + alphabet[doubleDigit]);
            }
       }
    } 

    _backtracking(message, '');

    return codes.size;
}