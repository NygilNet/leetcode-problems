/*
This problem was asked by Two Sigma.

Ghost is a two-person word game where players alternate appending letters to a word. The first person who spells out a word, or creates a prefix for which there is no possible continuation, loses. Here is a sample game:

Player 1: g
Player 2: h
Player 1: o
Player 2: s
Player 1: t [loses]
Given a dictionary of words, determine the letters the first player should start with, such that with optimal play they cannot lose.

For example, if the dictionary is ["cat", "calf", "dog", "bear"], the only winning start letter would be b.


*/

public static void GhostGame(string[] dictionary)
{

}

public class TrieNode
{
    private Dictionary<char, TrieNode> kids;
    private bool isEndOfWord;

    public Dictionary<char, TrieNode> Kids
    {
        get => kids;
        set => kids = value;
    }

    public bool IsEndOfWord
    {
        get => isEndOfWord;
        set => isEndOfWord = value;
    }

    public TrieNode()
    {
        Kids = new Dictionary<char, TrieNode>();
        IsEndOfWord = false;
    }
}

public class Trie
{
    private static TrieNode root;

    public static TrieNode Root
    {
        get => root;
        set => root = value;
    }

    public Trie()
    {
        Root = new TrieNode();
    }

    private static (bool, TrieNode?) Traverse(string s)
    {
        TrieNode? current = Root;

        foreach (char c in s)
        {
            if (!current.Kids.TryGetValue(c, out current))
                return (false, null);
        }

        return (true, current);
    }

    public void Insert(string word)
    {
        TrieNode currentNode = root;

        foreach (char c in word)
        {
            if (!currentNode.Kids.ContainsKey(c))
                currentNode.Kids[c] = new TrieNode();
            currentNode = currentNode.Kids[c];
        }

        currentNode.IsEndOfWord = true;
    }

    public bool Search(string word)
    {
        (bool res, TrieNode? node) = Traverse(word);

        if (res && node != null)
            return node.IsEndOfWord;
        return res;
    }

    public bool StartsWith(string prefix)
    {
        (bool res, _) = Traverse(prefix);
        return res;
    }
}
