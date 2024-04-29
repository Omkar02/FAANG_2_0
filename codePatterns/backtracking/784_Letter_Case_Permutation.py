"""
* Example 1:
    Input: s = "a1b2"
    Output: ["a1b2","a1B2","A1b2","A1B2"]
* Example 2:
    Input: s = "3z4"
    Output: ["3z4","3Z4"]

"""


def letterCasePermutation(s: str) -> list[str]:
    res = []

    def _backtrack(idx: int, s_arr: list[str]):
        if idx == len(s):
            res.append("".join(s_arr))
        else:
            if s_arr[idx].isalpha():
                s_arr[idx] = s_arr[idx].upper()
                _backtrack(idx+1, s_arr)

                s_arr[idx] = s_arr[idx].lower()
                _backtrack(idx + 1, s_arr)
            else:
                _backtrack(idx + 1, s_arr)

    _backtrack(0, list(s))
    return res


print(letterCasePermutation(s="a1b2"))
print(letterCasePermutation(s="3z4"))
