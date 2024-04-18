"""
* Example 1:
    Input: n = 2, trust = [[1,2]]
    Output: 2
* Example 2:
    Input: n = 3, trust = [[1,3],[2,3]]
    Output: 3
* Example 3:
    Input: n = 3, trust = [[1,3],[2,3],[3,1]]
    Output: -1

"""


def findJudge(n: int, trust: list[list[int]]) -> int:
    """
    *. If the town judge exists, then:
    ?.  The town judge trusts nobody.
    ?.  Everybody (except for the town judge) trusts the town judge.
    ?.  There is exactly one person that satisfies properties 1 & 2
    """
    trust_conn = {x: 0 for x in range(1, n+1)}
    for t in trust:
        # * Making a trust dict wherenin if someone is trusting
        # * the persons number is dec by -1 and +1 to people who they trust
        person, trusts = t[0], t[1]
        trust_conn[trusts] += 1
        trust_conn[person] -= 1

    # * at the end loop through all the persons to find val == n-1
    # * n-1 as the same person cant trust himself.
    judge = [key for key, val in trust_conn.items() if val == n-1]
    return judge[0] if judge else -1


print(findJudge(n=2, trust=[[1, 2]]))
print(findJudge(n=3, trust=[[1, 3], [2, 3]]))
print(findJudge(n=3, trust=[[1, 3], [2, 3], [3, 1]]))

print(findJudge(n=3, trust=[[1, 2], [2, 3]]))
