"""
? Pattern: DP on string
? Approach: TOP DOWN | Reccurssion + Memoization
? O(N x M)

* Example 1:
    Input: text1 = "abcde", text2 = "ace" 
    Output: 3  
    Explanation: The longest common subsequence is "ace" and its length is 3.
* Example 2:
    Input: text1 = "abc", text2 = "abc"
    Output: 3
    Explanation: The longest common subsequence is "abc" and its length is 3.
* Example 3:
    Input: text1 = "abc", text2 = "def"
    Output: 0
    Explanation: There is no such common subsequence, so the result is 0.
"""


def longestCommonSubsequence(text1: str, text2: str) -> int:
    len_one = len(text1) - 1
    len_two = len(text2) - 1
    cache = {}

    def _getLCS(idx1: int, idx2: int) -> int:
        key = (idx1, idx2)
        if key in cache:
            return cache[key]

        if idx1 < 0 or idx2 < 0:
            return 0
        if text1[idx1] == text2[idx2]:
            cache[key] = 1 + _getLCS(idx1 - 1, idx2 - 1)
            return cache[key]

        cache[key] = max(_getLCS(idx1 - 1, idx2), _getLCS(idx1, idx2 - 1))
        return cache[key]
    return _getLCS(len_one, len_two)


# print(longestCommonSubsequence(text1="abcde", text2="ace"))
# print(longestCommonSubsequence(text1="abc", text2="abc"))
# print(longestCommonSubsequence(text1="abc", text2="def"))

print(longestCommonSubsequence(text1="abac", text2="cab"))
