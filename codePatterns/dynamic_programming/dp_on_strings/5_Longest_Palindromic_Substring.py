"""
? Pattern: DP on string
? Approach: TOP DOWN | Reccurssion + Memoization

* Example 1:
    Input: s = "babad"
    Output: "bab"
    Explanation: "aba" is also a valid answer.
* Example 2:
    Input: s = "cbbd"
    Output: "bb"
"""


def longestPalindrome(s: str) -> str:
    len_s = len(s)
    longest_pali = ""

    def isPali(left: int, right: int) -> int:
        while (left >= 0 and right < len_s) and (s[left] == s[right]):
            left -= 1
            right += 1
        return s[left+1:right]

    for idx in range(len_s):
        odd_pali = isPali(idx, idx+1)
        even_pali = isPali(idx, idx)

        longest_pali = max(longest_pali, odd_pali, even_pali,
                           key=lambda x: len(x))
    return longest_pali


print(longestPalindrome(s="babad"))
print(longestPalindrome(s="cbbd"))
