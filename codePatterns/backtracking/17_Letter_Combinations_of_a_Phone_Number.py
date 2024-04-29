"""
* Example 1:
    Input: digits = "23"
    Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
* Example 2:
    Input: digits = ""
    Output: []
* Example 3:
    Input: digits = "2"
    Output: ["a","b","c"]
"""

MAPPING = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz'
}


def letterCombinations(digits: str) -> list[str]:
    res = []
    n = len(digits)

    def _backtrack(idx: int, typed_char: str):
        if len(typed_char) == n:
            res.append(typed_char)
        else:
            for letter in MAPPING[digits[idx]]:
                _backtrack(idx+1, typed_char + letter)

    _backtrack(0, "")
    return res


print(letterCombinations(digits="23"))
print(letterCombinations(digits=""))
print(letterCombinations(digits="2"))
