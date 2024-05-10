"""
? Pattern: Minimum (Maximum) Path to Reach a Target
? Approach: TOP DOWN | Reccurssion + Memoization
* Example 1:
    Input: n = 12
    Output: 3
    Explanation: 12 = 4 + 4 + 4.
* Example 2:
    Input: n = 13
    Output: 2
    Explanation: 13 = 4 + 9.

"""


# def numSquares(n: int) -> int:
#     # * For getting all the nessary perfect square
#     # * we need to have the last value of it
#     # * Thus taking a suqare root of and adding 1 gives, the END
#     end = int(n ** 0.5)
#     perfect_sq_arr = [x ** 2 for x in range(1, end + 1)]
#     cache = {}

#     def _getMinPerfectSqReq(idx: int, curr_arr: list) -> int:
#         # ? the key here is a 3D ke haveing unique idx, len_cur_arr and sum_curr_arr
#         key = (idx, len(curr_arr), sum(curr_arr))

#         if key in cache:
#             return cache[key]
#         if idx > end or sum(curr_arr) > n:
#             # ! Boundry Case to avoid overflow.
#             return float('inf')
#         if sum(curr_arr) == n:
#             return len(curr_arr)

#         min_sq_req = float('inf')
#         for jdx in range(idx, end):
#             curr_arr.append(perfect_sq_arr[jdx])
#             # * here JDX is used to make sure same ele can be used multiple time(duplicate)
#             min_sq_req = min(min_sq_req, _getMinPerfectSqReq(jdx, curr_arr))
#             curr_arr.pop()

#         cache[key] = min_sq_req
#         return cache[key]

#     return _getMinPerfectSqReq(0, [])


def numSquares(n: int) -> int:
    end = int(n ** 0.5)
    prefect_sq_arr = [x**2 for x in range(1, end + 1)]
    cache = {}

    def _geMinPerfSqReq(idx, cur_val):
        key = cur_val
        if key in cache:
            return cache[key]
        if idx > end or cur_val < 0:
            return float("inf")
        if cur_val == 0:
            return 0

        min_sq_req = float('inf')
        for jdx in range(idx, end):
            min_sq_req = min(min_sq_req,
                             1 + _geMinPerfSqReq(jdx, cur_val-prefect_sq_arr[jdx]))
        cache[key] = min_sq_req
        return cache[key]
    return _geMinPerfSqReq(0, n)


print(numSquares(n=12))
print(numSquares(n=13))
print(numSquares(n=50))
print(numSquares(n=149))
