"""
* Example 1:
    Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
    Output: true
    Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.
* Example 2:
    Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
    Output: false
    Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], 
    hence the sequence is unsorted.
* Example 3:
    Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
    Output: false
    Explanation: The first three characters "app" match, and the second string is 
    shorter (in size.) 
"""


def isAlienSorted(words: list[str], order: str) -> bool:
    return words == sorted(words, key=lambda words: [order.index(w) for w in words])


print(isAlienSorted(
    words=["hello", "leetcode"],
    order="hlabcdefgijkmnopqrstuvwxyz")
)

print(isAlienSorted(
    words=["word", "world", "row"],
    order="worldabcefghijkmnpqstuvxyz")
)

print(isAlienSorted(
    words=["apple", "app"],
    order="abcdefghijklmnopqrstuvwxyz")
)
