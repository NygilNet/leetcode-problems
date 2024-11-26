/*
This problem was asked by PayPal.

Given a string and a number of lines k, print the string in zigzag form. In zigzag, characters are printed out diagonally from top left to bottom right until reaching the kth line, then back up to top right, and so on.

For example, given the sentence "thisisazigzag" and k = 4, you should print:

t     a     g
 h   s z   a
  i i   i z
   s     g

*/

Solution solution = new Solution();
solution.PrintZigzag("thisisazigzag", 4);

class Solution 
{
    void PrintZigzag(string sentence, int k)
    {
        string[] lines = new string[k];
        Array.Fill(lines, "");
        int lineIndex = 0;
        bool indexAscending = true;

        for (int i = 0; i < sentence.Length; i++)
        {
            lines[lineIndex] += sentence[i].ToString().PadLeft(i - lines[lineIndexIndex].Length);
            if (indexAscending)
            {
                lineIndex++;
                if (lineIndex == k)
                {
                    indexAscending = false;
                    lineIndex = k - 2;
                }
            }
            else
            {
                lineIndex--;
                if (lineIndex == -1)
                {
                    indexAscending = true;
                    lineIndex = 1;
                }
            }
        } 

        foreach (string line in lines)
            Console.WriteLine(line);
        
    }
}

