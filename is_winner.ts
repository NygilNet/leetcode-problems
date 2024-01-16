/*

link to leetcode: https://leetcode.com/problems/determine-the-winner-of-a-bowling-game/

You are given two 0-indexed integer arrays player1 and player2, that represent the number of pins that player 1 and player 2 hit in a bowling game, respectively.

The bowling game consists of n turns, and the number of pins in each turn is exactly 10.

Assume a player hit xi pins in the ith turn. The value of the ith turn for the player is:

2xi if the player hit 10 pins in any of the previous two turns.
Otherwise, It is xi.
The score of the player is the sum of the values of their n turns.

Return

1 if the score of player 1 is more than the score of player 2,
2 if the score of player 2 is more than the score of player 1, and
0 in case of a draw.

*/

const STRIKE_SCORE = 10;

function calculateTurnScore(player: number[], index: number) {
    let currentTurn = player[index];
    let isStrike = player[index - 1] === STRIKE_SCORE || player[index - 2] === STRIKE_SCORE;
    return isStrike ? 2 * currentTurn : currentTurn;
}

function calculateTotalScore(player: number[]) {
    let totalScore = 0, length = player.length;
    for (let i = 0; i < length; i++) {
        totalScore += calculateTurnScore(player, i);
    }
    return totalScore;
}

function isWinner(player1: number[], player2: number[]): number {
    const player1Score = calculateTotalScore(player1);
    const player2Score = calculateTotalScore(player2);

    return player1Score > player2Score ? 1 : player1Score !== player2Score ? 2 : 0;
}

/*

A revised version of a leetcode question have completed

Changes made:

    used less ternary statements and added helper functions to make code more readable

*/