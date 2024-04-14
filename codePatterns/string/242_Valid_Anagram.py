"""
* Example 1: 
    Input: s = "anagram", t = "nagaram"
    Output: true
* Example 2: 
    Input: s = "rat", t = "car"
    Output: false
"""


def isAnagram(s: str, t: str) -> bool:
    """
    * Sol 1: using sorted
    * O(N) O(N)
    """
    return list(sorted(s)) == list(sorted(t))


def isAnagram(s: str, t: str) -> bool:
    """
    * Solution 2: this this with 
    * O(N) O(1)
    """
    if len(s) != len(t):
        return False

    def _get_word_count(word):
        wordCount = [0] * 26
        for idx in range(len(word)):
            wordCount[ord(word[idx]) - ord('a')] += 1
        return wordCount

    return _get_word_count(s) == _get_word_count(t)


print(isAnagram(s="anagram", t="nagaram"))
print(isAnagram(s="rat", t="car"))
