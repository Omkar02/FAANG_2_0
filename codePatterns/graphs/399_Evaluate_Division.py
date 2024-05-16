"""
* TYPE             : Graph
* ALGORITHM        : DFS 

* TIME-COMPLEXITY  :
* SPACE-COMPLEXITY :

* Example 1:
    Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
    Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
    Explanation: 
        Given: a / b = 2.0, b / c = 3.0
        queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? 
        return: [6.0, 0.5, -1.0, 1.0, -1.0 ]
        note: x is undefined => -1.0
* Example 2:
    Input: equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
    Output: [3.75000,0.40000,5.00000,0.20000]
* Example 3:
    Input: equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
    Output: [0.50000,2.00000,-1.00000,-1.00000]
"""


def calcEquation(equations: list[list[str]], values: list[float], queries: list[list[str]]) -> list[float]:
    div_values = {}
    # * ------------------------------------------------------------------------------

    def _DFS(src: int, dest: int, cur_val: int) -> float:
        """
        @param: src     : IT'S THE CUR NUMBER WE ARE ON FOR DIVISIBLITY
        @param: dest    : IT'S THE END NUMBER OF THE DIVISION
        @param: cur_val : IT'S THE RUNNING MUL. VALUE 
        """
        if src == dest:
            return cur_val

        visited.add(src)

        if src in div_values:
            for next_src, value in div_values[src].items():
                if next_src not in visited:
                    ans = _DFS(next_src, dest, cur_val * value)
                    if ans > -1:
                        return ans
        return -1
    # * ------------------------------------------------------------------------------
    for (x, y), val in zip(equations, values):
        if x not in div_values:
            div_values[x] = {}
        if y not in div_values:
            div_values[y] = {}

        div_values[x][y] = val
        div_values[y][x] = 1 / val

    # * {'a': {'b': 2.0}, 'b': {'a': 0.5, 'c': 3.0}, 'c': {'b': 0.3333333333333333}}
    # print(div_values)
    # * ------------------------------------------------------------------------------

    res = []
    visited = set()
    for x, y in queries:
        # * CHECK IF BOTH X AND Y ARE THERE IN THE DIV_VALUES
        if x in div_values and y in div_values:
            res.append(_DFS(x, y, 1))
            visited = set()
        else:
            res.append(-1)
    return res


print(calcEquation(equations=[["a", "b"], ["b", "c"]],
                   values=[2.0, 3.0],
                   queries=[["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]))

print(calcEquation(equations=[["a", "b"], ["b", "c"], ["bc", "cd"]],
                   values=[1.5, 2.5, 5.0],
                   queries=[["a", "c"], ["c", "b"], ["bc", "cd"], ["cd", "bc"]]))

print(calcEquation(equations=[["a", "b"]],
                   values=[0.5],
                   queries=[["a", "b"], ["b", "a"], ["a", "c"], ["x", "y"]]))
