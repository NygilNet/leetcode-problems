"""

This problem was asked by Amazon.

Given a string s and an integer k, break up the string into multiple lines such that each line has a length of k or less. You must break it up so that words don't break across lines. Each line has to have the maximum possible amount of words. If there's no way to break the text up, then return null.

You can assume that there are no spaces at the ends of the string and that there is exactly one space between each word.

For example, given the string "the quick brown fox jumps over the lazy dog" and k = 10, you should return: ["the quick", "brown fox", "jumps over", "the lazy", "dog"]. No string in the list has a length of more than 10.


Input: string, integer 
Output: array of strings (length of each string must be integer or less)


- initialize i @ 0 and ans as an empty array
- while i < length of s

    - slice string from i to i + k
    - iterate backwards in string to remove cut off word and white space
    - set i to i - (how ever many chars we had to iterate backwards from (+1 to account for white space))
    - append the string to the end of ans

- return ans
        

"""

def breakUpString(s: str, k: int) -> list[str]:
    pass