"""
* Example 1:
    Input: pattern = "abba", s = "dog cat cat dog"
    Output: true
* Example 2:
    Input: pattern = "abba", s = "dog cat cat fish"
    Output: false
* Example 3:
    Input: pattern = "aaaa", s = "dog cat cat dog"
    Output: false
"""


def wordPattern(pattern: str, s: str) -> bool:
    splited_s = s.split(" ")
    if len(splited_s) != len(pattern) or len(set(splited_s)) != len(set(pattern)):
        return False

    word_mapping = {}
    for idx, val in enumerate(pattern):
        if val not in word_mapping:
            word_mapping[val] = splited_s[idx]
        else:
            if word_mapping[val] != splited_s[idx]:
                return False

        print(word_mapping)
    return True


# print(wordPattern(pattern="abba", s="dog cat cat dog"))
# print(wordPattern(pattern="abba", s="dog cat cat fish"))
print(wordPattern(pattern="abba", s="dog dog dog dog"))
