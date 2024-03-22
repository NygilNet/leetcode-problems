/*

This problem was asked by Twitter.

Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, return all strings in the set that have s as a prefix.

For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].

Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.

*/

function autocomplete(query: string, set: string[]): string[] {
    const matches: string[] = [];
    for (const str of set) {
        if (str.slice(0, query.length).toLowerCase() === query.toLowerCase()) {
            matches.push(str);
        }
    }
    return matches;
}

/*

researching alternative solutions

    trie data structure


*/