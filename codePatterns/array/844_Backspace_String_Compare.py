"""
* Example 1:
    Input: s = "ab#c", t = "ad#c"
    Output: true
    Explanation: Both s and t become "ac".
* Example 2:
    Input: s = "ab##", t = "c#d#"
    Output: true
    Explanation: Both s and t become "".
* Example 3:
    Input: s = "a#c", t = "b"
    Output: false
    Explanation: s becomes "c" while t becomes "b".
"""


def backspaceCompare(s: str, t: str) -> bool:
    def evalute_stiring(word):
        _temp_stack = []
        for w in word:
            if _temp_stack and w == '#':
                _temp_stack.pop()
            elif w != '#':
                _temp_stack.append(w)
        return "".join(_temp_stack)

    return evalute_stiring(s) == evalute_stiring(t)


print(backspaceCompare(s="ab#c", t="ad#c"))
print(backspaceCompare(s="ab##", t="c#d#"))
print(backspaceCompare(s="a#c", t="b"))
print(backspaceCompare(s="y#fo##f", t="y#f#o##f"))
