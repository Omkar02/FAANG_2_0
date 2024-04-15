"""
* Example 1:
    Input: s = "babad"
    Output: "bab"
    Explanation: "aba" is also a valid answer.
* Example 2:
    Input: s = "cbbd"
    Output: "bb"
"""


def isPali(s, left, right):
    while left >= 0 and right < len(s):
        if s[left] != s[right]:
            break
        left -= 1
        right += 1
    return s[left+1:right]


def longestPalindrome(s: str) -> int:
    longest_pali = ""
    for idx in range(len(s)):
        even_pali = isPali(s, idx, idx)
        odd_pali = isPali(s, idx, idx+1)

        longest_pali = max(longest_pali, even_pali,
                           odd_pali, key=lambda x: len(x))
    return longest_pali


print(longestPalindrome(s="bab"))
print(longestPalindrome(s="cbbd"))
