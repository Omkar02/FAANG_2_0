"""
? Pattern: DP on string
? Approach: TOP DOWN | Reccurssion + Memoization
? O(N x M)

* Example 1:
    Input: s = "bbbab"
    Output: 4
    Explanation: One possible longest palindromic subsequence is "bbbb".
* Example 2:
    Input: s = "cbbd"
    Output: 2
    Explanation: One possible longest palindromic subsequence is "bb".
"""


def longestPalindromeSubseq(s: str) -> int:
    # * This is the best way; REFER IT
    len_s = len(s) - 1
    cache = {}

    def _getLongestSeq(left: int, right: int) -> int:
        key = (left, right)
        if key in cache:
            return cache[key]
        if left > right:
            return 0
        if s[left] == s[right]:
            length = 1 if left == right else 2
            cache[key] = length + _getLongestSeq(left + 1, right - 1)
            return cache[key]

        cache[key] = max(_getLongestSeq(left + 1, right),
                         _getLongestSeq(left, right-1))
        return cache[key]

    return _getLongestSeq(0, len_s)


# !--------------------------- BELOW SOL WORKS BUT IS MEMORY HEAVY ------------------------------------------------------!

def longestPalindromeSubseq(s: str) -> int:
    # ! NEETCODE SOL = https://www.youtube.com/watch?v=bUr8cNWI09Q&ab_channel=NeetCodeIO
    cache = {}
    s_len = len(s)

    def _getLongestSeq(left: int, right: int) -> int:
        key = (left, right)
        if key in cache:
            return cache[key]

        if left < 0 or right >= s_len:
            return 0

        if s[left] == s[right]:
            length = 1 if left == right else 2
            cache[key] = length + _getLongestSeq(left - 1, right + 1)
            return cache[key]

        else:
            cache[key] = max(_getLongestSeq(left - 1, right),
                             _getLongestSeq(left, right + 1))
            return cache[key]

    max_val = 0
    for idx in range(s_len):
        odd_pali = _getLongestSeq(idx, idx)
        even_pali = _getLongestSeq(idx, idx+1)
        max_val = max(max_val, odd_pali, even_pali)
    return max_val


print(longestPalindromeSubseq(s="bbbab"))
print(longestPalindromeSubseq(s="cbbd"))
