

function problem7(message) {

    const codes = [];
    const alphabet = "_abcdefghijklmnopqrstuvwxyz";
    const map = {};

    for (let i = 1; i < alphabet.length; i++) {
        map[i] = alphabet[i];
    }

    function _backtracking(queue, code) {
        if (!queue.length) {
            codes.push(code);
            return;
        }

        if (queue.length >= 1) {
            const singleCopy = [...queue];
            const singleKey = singleCopy.shift();
            if (!map[+singleKey]) {
                return;
            }
            _backtracking(singleCopy, code + map[singleKey]);
        } 
        if (queue.length >= 2) {
            const doubleCopy = [...queue];
            const doubleKey = doubleCopy.shift() + doubleCopy.shift();
            if (!map[+doubleKey]) {
                return;
            }
            _backtracking(doubleCopy, code + map[doubleKey]);
        }
    } 

    _backtracking(message.split(""), '');

    return codes;
}

console.log(problem7('111'));