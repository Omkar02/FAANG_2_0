"""
? Pattern: Decision Making
? Approach: TOP DOWN | Reccurssion + Memoization

* Example 1:
    Input: strs = ["10","0001","111001","1","0"], m = 5, n = 3
    Output: 4
    Explanation: The largest subset with at most 5 0's and 3 1's is {"10", "0001", "1", "0"}, so the answer is 4.
        Other valid but smaller subsets include {"0001", "1"} and {"10", "1", "0"}.
        {"111001"} is an invalid subset because it contains 4 1's, greater than the maximum of 3.
* Example 2:
    Input: strs = ["10","0","1"], m = 1, n = 1
    Output: 2
    Explanation: The largest subset is {"0", "1"}, so the answer is 2.
"""


def findMaxForm(strs: list[str], m: int, n: int) -> int:
    strs_len = len(strs)
    cache = {}

    def _getMaxArr(idx, cur_m, cur_n):
        key = (idx, cur_m, cur_n)
        if key in cache:
            return cache[key]

        if idx == strs_len:
            return 0
        zeros = strs[idx].count('0')
        ones = strs[idx].count('1')

        include = 0
        if zeros <= cur_m and ones <= cur_n:
            include = 1 + _getMaxArr(idx + 1, cur_m - zeros, cur_n - ones)

        exclude = _getMaxArr(idx + 1, cur_m, cur_n)

        cache[key] = max(include, exclude)
        return cache[key]

    return _getMaxArr(0, m, n)


print(findMaxForm(strs=["10", "0001", "111001", "1", "0"], m=5, n=3))
print(findMaxForm(strs=["10", "0", "1"], m=1, n=1))
print(findMaxForm(strs=["10", "0001", "111001", "1", "0"], m=4, n=3))
