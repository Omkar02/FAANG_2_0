"""
? Pattern: Distinct Ways
? Approach: TOP DOWN | Reccurssion + Memoization

Example 1:
    Input: nums = [1,5,11,5]
    Output: true
    Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:
    Input: nums = [1,2,3,5]
    Output: false
    Explanation: The array cannot be partitioned into equal sum subsets.
"""


def canPartition(nums: list[int]) -> bool:
    total_sum = sum(nums)

    if total_sum % 2 != 0:
        return False

    nums_len = len(nums)
    cache = {}

    def _canPartitions(idx: int, cur_sum: int) -> bool:
        key = (idx, cur_sum)
        if key in cache:
            return cache[key]
        if cur_sum == 0:
            # * FOR CUR_SUM GETTING 0 MEANING WE HAVE A PARTITION
            return True
        if idx == nums_len or cur_sum < 0:
            # ! BASE CONDITION
            #   ! AS WHEN IDX HAS REACHED AND CUR_SUM IS NOT 0
            #   ! OR CUR_SUM GET -VE
            return False

        # * CONSIDERING CUR IDX CAL BY SUBTRACTING FROM HALF TOTAL SUM
        consider = _canPartitions(idx + 1, cur_sum - nums[idx])
        # * NOT CONSIDERING AND MOVING FORWARD
        not_consider = _canPartitions(idx + 1, cur_sum)

        if consider or not_consider:
            cache[key] = True
        else:
            cache[key] = False

        return cache[key]

    # * HERE WE CHECK IF HALF OF TOTAL_SUM CAN BE CONSTRUCTED.
    return _canPartitions(0, total_sum // 2)


print(canPartition(nums=[1, 5, 11, 5]))
print(canPartition(nums=[1, 2, 3, 5]))
print(canPartition(nums=[1, 2, 5]))
print(canPartition(nums=[14, 75, 64, 20, 95, 78, 6, 98, 77, 4, 71, 66, 78, 44, 4, 46, 77, 46, 4, 84, 18, 14, 52, 5, 89, 26, 12, 48, 71, 35, 57, 10, 59, 69, 35, 70, 34, 80, 80, 66, 91, 9, 36, 91, 85, 24, 46,
      45, 54, 86, 3, 40, 30, 23, 24, 4, 88, 50, 42, 25, 41, 60, 27, 47, 92, 92, 49, 50, 56, 94, 9, 82, 49, 41, 18, 1, 23, 85, 8, 48, 55, 59, 82, 82, 12, 84, 47, 45, 41, 28, 22, 15, 50, 9, 64, 91, 6, 94, 14, 31]))
