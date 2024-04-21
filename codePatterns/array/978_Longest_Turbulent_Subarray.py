"""
* Example 1:
    Input: arr = [9,4,2,10,7,8,8,1,9]
    Output: 5
    Explanation: arr[1] > arr[2] < arr[3] > arr[4] < arr[5]
* Example 2:
    Input: arr = [4,8,12,16]
    Output: 2
* Example 3:
    Input: arr = [100]
    Output: 1
"""


def maxTurbulenceSize(arr: list[int]) -> int:
    """
    * This is a sliding window approch
    Time = O(N)
    Space = O(1)
    """
    max_len = float("-inf")
    left = right = 0
    arr_len = len(arr)

    def isTurbulent(x): return True if (
        arr[x-1] > arr[x] < arr[x+1]) or (arr[x-1] < arr[x] > arr[x+1]) else False

    while right < arr_len:
        while left < arr_len - 1 and arr[left] == arr[left+1]:
            """
            * This takes care of the duplicates like 8, and we need to ignore them. 
            * Eg.: [..., 10, 7, 8, 8, 1, ...]
            """
            left += 1
        while right < arr_len - 1 and isTurbulent(right):
            right += 1

        max_len = max(max_len, right - left + 1)
        left = right
        right += 1
    print(max_len)
    return max_len


assert maxTurbulenceSize(arr=[9, 4, 2, 10, 7, 8, 8, 1, 9]) == 5
assert maxTurbulenceSize(arr=[4, 8, 12, 16]) == 2
assert maxTurbulenceSize(arr=[100]) == 1
