"""
? Pattern: Distinct Ways
? Approach: TOP DOWN | Reccurssion + Memoization
~
* Example 1:
    Input: nums = [1,3,5,4,7]
    Output: 2
    Explanation: The two longest increasing subsequences are [1, 3, 4, 7] and [1, 3, 5, 7].
* Example 2:
    Input: nums = [2,2,2,2,2]
    Output: 5
    Explanation: The length of the longest increasing subsequence is 1,
                 and there are 5 increasing subsequences of length 1, so output 5.

! VIDEO EXPLAINATION = https://www.youtube.com/watch?v=Tuc-rjJbsXU&ab_channel=NeetCode
"""


def findNumberOfLIS(nums: list[int]) -> int:
    """
    ? THE QUESTION HERE IS TO GET THE NO. OF LIS
    """
    nums_len = len(nums)
    # ? dp = maintains an array = [length_LIS, count_LIS]
    dp = {}

    # ? max_len_lis =  maintains the len of max LIS
    # ? res = maintains count of how many LIS are present with same len
    max_len_lis, res = 0, 0

    for idx in reversed(range(nums_len)):
        # * BOTH ARE 1 AS CONSIDETING THE CUR IDX AS AND ELE AND THE CUR_MAX IS 1 ELEMENT
        cur_max, sq_count = 1, 1

        for jdx in range(idx, nums_len):
            # PROCESSING IN REVERSE ORDER
            if nums[jdx] > nums[idx]:
                # Only Processing for if JDX is increasing
                length, count = dp[jdx]

                if length + 1 > cur_max:
                    # * IF THE CUR_LEN IS GREATER THEN REPLACE BOTHE LEN AND COUNT
                    cur_max = length + 1
                    sq_count = count
                elif length + 1 == cur_max:
                    # * IF CUR_LEN IS EQUAL THEN ADD THE COUNT
                    sq_count += count

        # ? ---- USED TO UPDATED THE MAX AND RES ----
        if cur_max > max_len_LIS:
            max_len_LIS = cur_max
            res = sq_count
        elif cur_max == max_len_lis:
            res += sq_count
        # ? -----------------------------------------

        # * CACHE THE CUR_MAX AND SQ_COUNT AT THAT IDX
        dp[idx] = [cur_max, sq_count]
    return res


print(findNumberOfLIS(nums=[1, 3, 5, 4, 7]))
print(findNumberOfLIS(nums=[2, 2, 2, 2, 2]))
