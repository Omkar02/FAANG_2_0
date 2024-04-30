"""
* Example 1:
    Input: n = 3
    Output: ["((()))","(()())","(())()","()(())","()()()"]
* Example 2:
    Input: n = 1
    Output: ["()"]
"""


def generateParenthesis(n: int) -> list[str]:
    def isValid(brackets: str) -> bool:
        cnt = 0
        for b in brackets:
            cnt = cnt+1 if b == '(' else cnt - 1
            if cnt < 0:
                return False
        return cnt == 0

    def _backtrack(left: int, right: int, cur_brack: str):

        if len(cur_brack) == 2 * n and isValid(cur_brack):
            res.append(cur_brack)
            return
        if left < n:
            _backtrack(left+1, right, cur_brack+"(")

        if right < n:
            _backtrack(left, right+1, cur_brack + ")")
    res = []
    _backtrack(0, 0, "")
    return res


print(generateParenthesis(n=3))
print(generateParenthesis(n=1))
