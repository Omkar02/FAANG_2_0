"""
? Pattern: Distinct Ways
? Approach: TOP DOWN | Reccurssion + Memoization

* Example 1:
    Input: nums1 = [1,3,5,4], nums2 = [1,2,3,7]
    Output: 1
    Explanation: 
        Swap nums1[3] and nums2[3]. Then the sequences are:
        nums1 = [1, 3, 5, 7] and nums2 = [1, 2, 3, 4]
        which are both strictly increasing.
* Example 2:
    Input: nums1 = [0,3,5,8,9], nums2 = [2,1,4,6,9]
    Output: 1
"""


def minSwap(nums1: list[int], nums2: list[int]) -> int:
    nums1_len = len(nums1)
    cache = {}

    def _getMinSwaps(idx: int, pre_one: int, pre_two: int) -> int:
        key = (idx, pre_one, pre_two)
        if key in cache:
            return cache[key]

        if idx == nums1_len:
            return 0

        swap = no_swap = float('inf')
        if nums1[idx] > pre_one and nums2[idx] > pre_two:
            # * NO SWAP IS REQUIRED ALL IN PLACE.
            no_swap = _getMinSwaps(idx + 1, nums1[idx], nums2[idx])
        if nums2[idx] > pre_one and nums1[idx] > pre_two:
            # * SWAP IS REQURED BETWEEN THE ARR.
            swap = 1 + _getMinSwaps(idx + 1, nums2[idx], nums1[idx])

        cache[key] = min(swap, no_swap)
        return cache[key]

    return _getMinSwaps(0, -1, -1)


print(minSwap(nums1=[1, 3, 5, 4], nums2=[1, 2, 3, 7]))
print(minSwap(nums1=[0, 3, 5, 8, 9], nums2=[2, 1, 4, 6, 9]))
