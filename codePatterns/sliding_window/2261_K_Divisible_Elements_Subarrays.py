def countDistinct(nums: list[int], k: int, p: int) -> int:
    nums_len = len(nums)
    res = set()
    for idx in range(nums_len):
        count = 0
        for jdx in range(idx, nums_len):
            if nums[jdx] % 2 == 0:
                count += 1
            if count > k:
                break
            res.add(tuple(nums[idx:jdx + 1]))

    # * THE SET IS USED HERE TO MAINTAIN THE DISTINCT COUNT.
    # return f'res = {res} | len = {len(res)}'
    return len(res)


print(countDistinct(nums=[2, 3, 3, 2, 2], k=2, p=2))
print(3 % 2 == 0)
