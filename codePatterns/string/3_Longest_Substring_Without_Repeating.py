"""
* Example 1:
    Input: s = "abcabcbb"
    Output: 3
    Explanation: The answer is "abc", with the length of 3.

* Example 2:
    Input: s = "bbbbb"
    Output: 1
    Explanation: The answer is "b", with the length of 1.

* Example 3:
    Input: s = "pwwkew"
    Output: 3
    Explanation: The answer is "wke", with the length of 3.
    Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""


def lengthOfLongestSubstring(s: str) -> int:
    seen = set()
    maxLen = float("-inf")
    left = right = 0
    while right < len(s):
        if s[right] in seen:
            seen.remove(s[left])
            left += 1
        else:
            seen.add(s[right])
            right += 1
        maxLen = max(maxLen, right - left)
    return maxLen


print(lengthOfLongestSubstring(s="abcabcbb"))
print(lengthOfLongestSubstring(s="bbbbb"))
