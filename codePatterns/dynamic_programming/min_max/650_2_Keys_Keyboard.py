"""
? Pattern: Decision Making
? Approach: TOP DOWN | Reccurssion + Memoization

* Example 1:
    Input: n = 3
    Output: 3
    Explanation: Initially, we have one character 'A'.
                 In step 1, we use Copy All operation.
                 In step 2, we use Paste operation to get 'AA'.
                 In step 3, we use Paste operation to get 'AAA'.
* Example 2:
    Input: n = 1
    Output: 0
"""


def minSteps(n: int) -> int:
    """
        * We start with 1 A on screen and with an empty clipboard,
        ? In every iteration we have two options either we paste previously copied data or copy the current data and then paste it
        * Now, keep in mind that we can only paste if we have something in clipboard, if clipboard is empty we cannot paste

        For base case, since out target is to get n A's on screen, we return 0 
        when screen == n and if A's on screen becomes greater than n then we 
        need to discard this so we return Infinty, since we take min this will be discarded
    """
    cache = {}

    def _getMinSteps(screen: int, clipboard: int) -> int:
        key = (screen, clipboard)
        if key in cache:
            return cache[key]
        if screen == n:
            return 0
        if screen >= n:
            return float('inf')

        copy_and_paste = 2 + _getMinSteps(screen + screen, screen)
        paste = float('inf')
        if clipboard:
            paste = 1 + _getMinSteps(screen + clipboard, clipboard)

        cache[key] = min(copy_and_paste, paste)
        return cache[key]

    return _getMinSteps(1, 0)


print(minSteps(n=3))
print(minSteps(n=1))
