"""
* Example 1:
Input: name = "alex", typed = "aaleex"
Output: true
Explanation:'a' and 'e' in 'alex' were long pressed

* Example 2:
Input: name = "saeed", typed = "ssaaedd"
Output: false
Explanation:'e' must have been pressed twice, but it wasn't in the typed output.
"""


def printOutput(func):
    def _wrapper(*args, **kwargs):
        _res = func(*args, **kwargs)
        print(f'name: {args[0]} typed: {args[1]}\n', _res)
        return _res
    return _wrapper


@printOutput
def longPressedName(name, typed):
    nIdx = tIdx = 0
    nLen, tLen = len(name), len(typed)

    # * GOING 1 index with <= for only nIdx further as to make sure all are covered
    while nIdx <= nLen and tIdx < tLen:
        if nIdx < nLen and name[nIdx] == typed[tIdx]:
            nIdx += 1
            tIdx += 1
        elif nIdx and name[nIdx-1] == typed[tIdx]:
            tIdx += 1
        else:
            return False

    return nIdx == nLen and tIdx == tLen


name = "alex"
typed = "aaleex"
assert longPressedName(name, typed) == True

name = "saeed"
typed = "ssaaedd"
assert longPressedName(name, typed) == False


name = "leelee"
typed = "lleeelee"
assert longPressedName(name, typed) == True


name = "laiden"
typed = "laiden"
assert longPressedName(name, typed) == True

# ! Edge Case: for ending
name = 'vtkgn'
typed = 'vttkgnn'
assert longPressedName(name, typed) == True

# ! Edge Case: for starting
name = 'zlexya'
typed = 'aazlllllllllllllleexxxxxxxxxxxxxxxya'
assert longPressedName(name, typed) == False
