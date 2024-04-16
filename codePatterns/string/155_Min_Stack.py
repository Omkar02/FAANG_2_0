"""
* Example 1:
    Input
        ["MinStack","push","push","push","getMin","pop","top","getMin"]
        [[],[-2],[0],[-3],[],[],[],[]]

    Output
    [null,null,null,null,-3,null,0,-2]

    Explanation
    MinStack minStack = new MinStack();
    minStack.push(-2);
    minStack.push(0);
    minStack.push(-3);
    minStack.getMin(); // return -3
    minStack.pop();
    minStack.top();    // return 0
    minStack.getMin(); // return -2

"""


class MinStack:
    def __init__(self):
        self.stack = []
        self._min_val = []

    def push(self, val: int) -> None:
        self._min_val.append(
            min(self._min_val[-1], val) if self._min_val else val)
        self.stack.append(val)

    def pop(self) -> None:
        self._min_val.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self._min_val[-1]


minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
assert minStack.getMin() == -3  # return -3
minStack.pop()
assert minStack.top() == 0  # return 0
assert minStack.getMin() == -2  # return -2
