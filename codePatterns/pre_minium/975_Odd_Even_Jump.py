"""
    * Time Complexity   : O(NLogN)
    * Space Complexity  : O(N)
    * Date              : 3, June 2024
"""

"""
* Example 1:
    Input: arr = [10,13,12,14,15]
    Output: 2
    Explanation: 
        From starting index i = 0, we can make our 1st jump to i = 2 (since arr[2] is the smallest among arr[1], arr[2], arr[3], arr[4] that is greater or equal to arr[0]), then we cannot jump any more.
        From starting index i = 1 and i = 2, we can make our 1st jump to i = 3, then we cannot jump any more.
        From starting index i = 3, we can make our 1st jump to i = 4, so we have reached the end.
        From starting index i = 4, we have reached the end already.
        In total, there are 2 different starting indices i = 3 and i = 4, where we can reach the end with some number of
        jumps.
* Example 2:
    Input: arr = [2,3,1,1,4]
    Output: 3
    Explanation: 
        From starting index i = 0, we make jumps to i = 1, i = 2, i = 3:
        During our 1st jump (odd-numbered), we first jump to i = 1 because arr[1] is the smallest value in [arr[1], arr[2], arr[3], arr[4]] that is greater than or equal to arr[0].
        During our 2nd jump (even-numbered), we jump from i = 1 to i = 2 because arr[2] is the largest value in [arr[2], arr[3], arr[4]] that is less than or equal to arr[1]. arr[3] is also the largest value, but 2 is a smaller index, so we can only jump to i = 2 and not i = 3
        During our 3rd jump (odd-numbered), we jump from i = 2 to i = 3 because arr[3] is the smallest value in [arr[3], arr[4]] that is greater than or equal to arr[2].
        We can't jump from i = 3 to i = 4, so the starting index i = 0 is not good.
        In a similar manner, we can deduce that:
        From starting index i = 1, we jump to i = 4, so we reach the end.
        From starting index i = 2, we jump to i = 3, and then we can't jump anymore.
        From starting index i = 3, we jump to i = 4, so we reach the end.
        From starting index i = 4, we are already at the end.
        In total, there are 3 different starting indices i = 1, i = 3, and i = 4, where we can reach the end with some
        number of jumps.
* Example 3:
    Input: arr = [5,1,3,4,2]
    Output: 3
    Explanation: We can reach the end from starting indices 1, 2, and 4.
"""


def oddEvenJumps(arr: list[int]) -> int:
    n = len(arr)
    cache = {}

    # * ------------------ Pre-Processing ------------------
    # * Using a stack to find next_higher(even_jumps) and next_lower(odd_jumps)
    next_odd_jump = [-1] * n
    next_even_jump = [-1] * n

    # * Create a smaller idx-value
    stack = []
    for _, idx in sorted([a, i] for i, a in enumerate(arr)):
        while stack and stack[-1] < idx:
            next_odd_jump[stack.pop()] = idx
        stack.append(idx)

    # * Create a larger idx-value
    stack = []
    for _, idx in sorted([-a, i] for i, a in enumerate(arr)):
        while stack and stack[-1] < idx:
            next_even_jump[stack.pop()] = idx
        stack.append(idx)

    print(next_odd_jump, next_even_jump)
    # * ------------------------------------------------------

    def _can_jump(idx, is_odd_jump) -> bool:
        key = (idx, is_odd_jump)
        if key in cache:
            return cache[key]

        nonlocal n
        if idx == n - 1:
            return True

        # * ---------------------------  Not Optimised Way ---------------------------
        # next_jump_index = -1
        # if is_odd_jump:
        #     # * Find the smallest index j such that arr[idx] <= arr[jdx]
        #     for jdx in range(idx + 1, n):  # +1 to avoid duplicates
        #         if arr[idx] <= arr[jdx]:
        #             # * GET THE SMALLEST POSSIBLE VALUE
        #             if next_jump_index == -1 or arr[jdx] < arr[next_jump_index]:
        #                 next_jump_index = jdx

        # else:
        #     # * Find the largest index j such that arr[idx] >= arr[jdx]
        #     for jdx in range(idx + 1, n):  # +1 to avoid duplicates
        #         if arr[idx] >= arr[jdx]:
        #             if next_jump_index == -1 or arr[jdx] > arr[next_jump_index]:
        #                 next_jump_index = jdx
        # * ------------------------------------------------------------------------

        # * -------- Using Pre-Processed Values To Get The next-jump-idx -------
        next_jump_index = next_odd_jump[idx] if is_odd_jump else next_even_jump[idx]
        # * ------------------------------------------------------------------------

        # print('Odd Jump = ' if is_odd_jump else 'Even Jump = ', next_jump_index)
        if next_jump_index == -1:
            cache[key] = False
        else:
            cache[key] = _can_jump(next_jump_index, not is_odd_jump)
        return cache[key]

    good_index = 0

    for idx in range(n):
        if _can_jump(idx, True):
            good_index += 1

    return good_index


print(oddEvenJumps(arr=[10, 13, 12, 14, 15]))
print(oddEvenJumps(arr=[2, 3, 1, 1, 4]))
print(oddEvenJumps(arr=[5, 1, 3, 4, 2]))
