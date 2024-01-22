/*

link to problem: https://leetcode.com/problems/fizz-buzz/description/

Given an integer n, return a string array answer (1-indexed) where:

answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i (as a string) if none of the above conditions are true.

*/

function fizzBuzz(n: number): string[] {

    let answer: string [] = [];

    for (let i = 1; i <= n; i++) {
        let str = "";

        if (i % 3 === 0) str += "Fizz";
        if (i % 5 === 0) str += "Buzz";

        str = str || `${i}`;

        answer.push(str);
    }
    

    return answer;

}

/*

Seen a solution recently to remember

adding to a string instead of a block of if/else statements makes the code more readable and more able to maintain 


*/