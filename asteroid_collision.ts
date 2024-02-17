/*

link to leetcode: https://leetcode.com/problems/asteroid-collision/description/

We are given an array asteroids of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.


stack can be helpful because we may have to continuously destroy asteroids


// if stack is empty, append asteroid to stack
// if two asteroids with different signs

    // if top of stack is neg and new asteroid is pos, append asteroid to stack

    // if top of stack is pos and new asteroid is neg, compare abs values
        
        // as1 > as2, don't add ast2

        // as1 === as2, pop off ast1

        // as1 < as2, keep checking top of stack

// two asteroids with same signs, append asteroid to stack

*/

function asteroidCollision(asteroids: number[]): number[] {
    const stateOfAsteroids: number[] = [];

    for (const asteroid of asteroids) {
        while (stateOfAsteroids.length !== 0 && asteroid < 0 && stateOfAsteroids.at(-1) > 0) {
            if (Math.abs(asteroid) > stateOfAsteroids.at(-1))
        }

        stateOfAsteroids.push(asteroid);
    }

    return stateOfAsteroids;
}

//stack is helpful for repeated work