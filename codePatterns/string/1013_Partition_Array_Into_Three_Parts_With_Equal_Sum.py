"""
* Example 1:
    Input: arr = [0,2,1,-6,6,-7,9,1,2,0,1]
    Output: true
    Explanation:0 + 2 + 1 = -6 + 6 - 7 + 9 + 1 = 2 + 0 + 1
* Example 2:
    Input: arr = [0,2,1,-6,6,7,9,-1,2,0,1]
    Output: false
* Example 3:
    Input: arr = [3,3,6,5,-2,2,5,1,-9,4]
    Output: true
    Explanation:3 + 3 = 6 = 5 - 2 + 2 + 5 + 1 - 9 + 4
"""


def canThreePartsEqualSum(arr: list[int]) -> bool:
    # ! check if the partitions can be done
    t_sum = sum(arr)
    if t_sum % 3 != 0:
        return False

    parts = curr_sum = 0
    # divide the t_sum in equal parts
    part_sum = t_sum // 3
    for val in arr:
        curr_sum += val
        if curr_sum == part_sum:
            if parts == 2:
                return True
            parts += 1
            curr_sum = 0
    return False


print(canThreePartsEqualSum(arr=[0, 2, 1, -6, 6, -7, 9, 1, 2, 0, 1]))
print(canThreePartsEqualSum(arr=[0, 2, 1, -6, 6, 7, 9, -1, 2, 0, 1]))
print(canThreePartsEqualSum(arr=[3, 3, 6, 5, -2, 2, 5, 1, -9, 4]))
