"""
* Description
    Given a string S, find the length of the longest
    substring T that contains at most k distinct characters.
* Example 1:
    Input: S = "eceba" and k = 3
    Output: 4
    Explanation: T = "eceb"
* Example 2:
    Input: S = "WORLD" and k = 4
    Output: 4
    Explanation: T = "WORL" or "ORLD"
"""


# def longestSubstringWithKDistinctChar(s: str, k: int) -> int:
#     seen_dict = {}
#     curLen, maxLen = 0, float('-inf')
#     p1 = p2 = 0
#     while p2 < len(s):
#         if s[p2] not in seen_dict or seen_dict[s[p2]] == 0:
#             curLen += 1
#             seen_dict[s[p2]] = 0
#         seen_dict[s[p2]] += 1
#         p2 += 1

#         while curLen > k:
#             print('-'*20)
#             seen_dict[s[p1]] -= 1
#             if seen_dict[s[p1]] == 0:
#                 curLen -= 1
#             p1 += 1
#             print('\t', seen_dict, '\n', '-'*20)
#         print(p2, p1, seen_dict)
#         maxLen = max(maxLen, p2 - p1)
#     return maxLen


def longestSubstringWithKDistinctChar(s: str, k=int) -> int:
    visited_and_char_count = {}
    s_len = len(s)
    left = right = 0
    currDistinctCharCount = 0
    maxLen = float('-inf')

    while right < s_len:
        if s[right] not in visited_and_char_count or visited_and_char_count[s[right]] == 0:

            # ? check if the currWord i.e s[right] is first seen !
            # !OR
            # ? seen before but not considering in current maxLen
            currDistinctCharCount += 1  # ? inc the currDistinctCharCount to keep a track
            visited_and_char_count[s[right]] = 0
        visited_and_char_count[s[right]] += 1  # ? inc the R pointer val
        right += 1

        while currDistinctCharCount > k:
            # ! check if the currDistinctCharCount is not greated than k...
            # ! if its greated than increase the left pointer
            visited_and_char_count[s[left]] -= 1  # ? dec the L pointer val
            if visited_and_char_count[s[left]] == 0:
                # ? this is run as to make sure all the char are been considered
                # ? all the same char...
                currDistinctCharCount -= 1
            left += 1

        maxLen = max(maxLen, right - left)
    return maxLen


print(longestSubstringWithKDistinctChar(s="eceba", k=3))
print(longestSubstringWithKDistinctChar(s="WORLD", k=4))
print(longestSubstringWithKDistinctChar(s="aabcdef", k=4))
