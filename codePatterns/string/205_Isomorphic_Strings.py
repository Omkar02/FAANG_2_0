"""
* Example 1:
Input: s = "egg", t = "add"
Output: true

* Example 2:
Input: s = "foo", t = "bar"
Output: false
"""


def isIsomorphic(s: str, t: str) -> bool:
    """
    * why using zip ?
        zip() function would pair the first item 
        of first iterator (i.e s here) to the 
        first item of second iterator (i.e t here). 

        set() would remove duplicate items from the 
        zipped tuple. It is like the first item of first 
        iterator mapped to the first item of second iterator 
        as it would in case of a hashtable or dictionary.
    * O(N)
    """
    if len(s) != len(t):
        return False

    zippedSet = set(zip(s, t))
    return len(zippedSet) == len(set(s)) == len(set(t))


assert isIsomorphic(s="egg", t="add") == True
assert isIsomorphic(s="foo", t="bar") == False
assert isIsomorphic(s="bbbaaaba", t="aaabbbba") == False
