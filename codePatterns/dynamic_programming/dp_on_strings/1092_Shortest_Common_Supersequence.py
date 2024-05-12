"""
? Pattern: DP on string
? Approach: TOP DOWN | Reccurssion + Memoization


* Example 1:
    Input: str1 = "abac", str2 = "cab"
    Output: "cabac" acabac
    Explanation: 
        str1 = "abac" is a subsequence of "cabac" because we can delete the first "c".
        str2 = "cab" is a subsequence of "cabac" because we can delete the last "ac".
        The answer provided is the shortest such string that satisfies these properties.
* Example 2:
    Input: str1 = "aaaaaaaa", str2 = "aaaaaaaa"
    Output: "aaaaaaaa"
"""


def shortestCommonSupersequence(str1: str, str2: str) -> str:
    len_one = len(str1)
    len_two = len(str2)
    cache = {}

    def _longestCommonSubseq(idx1: int, idx2: int) -> str:
        key = (idx1, idx2)
        if key in cache:
            return cache[key]
        if not idx1 or not idx2:
            return ""

        if str1[idx1 - 1] == str2[idx2 - 1]:
            cache[key] = _longestCommonSubseq(
                idx1 - 1, idx2 - 1) + str1[idx1 - 1]
            return cache[key]

        cache[key] = max(_longestCommonSubseq(idx1 - 1, idx2),
                         _longestCommonSubseq(idx1, idx2 - 1),
                         key=lambda x: len(x))
        return cache[key]

    LCS = _longestCommonSubseq(len_one, len_two)
    print(f'LCS = {LCS}')
    idx_1 = idx_2 = 0  # * IDX'S ARE ONLY INIT ONCE...
    shortest_common_superseq = ""
    for char in LCS:
        while idx_1 < len_one and str1[idx_1] != char:
            shortest_common_superseq += str1[idx_1]
            idx_1 += 1

        while idx_2 < len_two and str2[idx_2] != char:
            shortest_common_superseq += str2[idx_2]
            idx_2 += 1

        shortest_common_superseq += char
        idx_1 += 1
        idx_2 += 1
    return shortest_common_superseq + str1[idx_1:] + str2[idx_2:]


print(shortestCommonSupersequence(str1="abac", str2="cab"))
print(shortestCommonSupersequence(str1="aaaaaaaa", str2="aaaaaaaa"))
print(shortestCommonSupersequence(str1="abcde", str2="ace"))

print(shortestCommonSupersequence(str1="bbbaaaba", str2="bbababbb"))
