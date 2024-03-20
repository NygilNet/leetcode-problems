/*

Input: sting
Output: sting (format `number`A`number`B)

first idea is to convert both strings into Sets

    - constant look up time
    - iterate thorugh secret 
        - if digit is in the set but in the wrong place increment cow count
            - if cow is set, remove that digit from the set
        - if digit is in set and in the right place incrment bull count

 */

        function getHint(secret: string, guess: string): string {
            let bulls: number = 0, cows: number = 0;
        
            const pairs: Map<string, number> = new Map();
        
            for (const char of secret) { 
                pairs.set(char, pairs.get(char) + 1 || 1);
            }
        
            // check for bulls
            for (let i = 0; i < guess.length; i++) { 
                if (secret[i] === guess[i]) {
                    bulls++;
                    pairs.set(guess[i], pairs.get(guess[i]) - 1);
                }
            }
        
            // check for cows
            for (let j = 0; j < guess.length; j++) {
                if (secret[j] !== guess[j] && pairs.get(guess[j])) {
                    cows++;
                    pairs.set(guess[j], pairs.get(guess[j])! - 1);
                }
            }
        
            return `${bulls}A${cows}B`;
        };