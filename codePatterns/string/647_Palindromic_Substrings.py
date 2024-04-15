"""
* Example 1:
    Input: s = "abc"
    Output: 3
    Explanation: Three palindromic strings: "a", "b", "c".
* Example 2:
    Input: s = "aaa"
    Output: 6
    Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
"""


def countSubstrings(s: str):
    def cache(func):
        _cache = {}

        def _wrapper(*args, **kwargs):
            print(_cache)
            if args in _cache:
                return _cache[args]
            _res = func(*args, **kwargs)
            _cache[args] = _res
            return _cache[args]
        return _wrapper

    @cache
    def isPali(x): return x == x[::-1]
    count = 0
    for idx in range(len(s)):
        for jdx in range(idx + 1, len(s) + 1):
            word = s[idx: jdx]
            if isPali(word):
                count += 1
    return count


# * Method 2: Odd & Even Pali count

def countSubstrings(s: str) -> int:
    count = 0
    for idx in range(len(s)):
        # ------- For even pali -------
        left, rigth = idx, idx
        while left >= 0 and rigth < len(s) and s[left] == s[rigth]:
            count += 1
            left -= 1
            rigth += 1
        # ------- For odd Pali -------
        left, rigth = idx, idx+1
        while left >= 0 and rigth < len(s) and s[left] == s[rigth]:
            count += 1
            left -= 1
            rigth += 1
    return count


print(countSubstrings(s="abc"))
print(countSubstrings(s="aaa"))
print(countSubstrings(
    s="dnncbwoneinoplypwgbwktmvkoimcooyiwirgbxlcttgteqthcvyoueyftiwgwwxvxvg"))
