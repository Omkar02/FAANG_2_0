"""
* TYPE             : Graph
* ALGORITHM        : BFS

* TIME-COMPLEXITY  : O(N)
* SPACE-COMPLEXITY : O(N)


* Example 1:
    Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
    Output: 5
    Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.
* Example 2:
    Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
    Output: 0
    Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.

"""


def ladderLength(beginWord: str, endWord: str, wordList: list[str]) -> int:
    beginWord_len = len(beginWord)

    # * CREATING A GRAPH WHICH WOULD BE HAVING ALL THE POSSIBLE COMBINITIONS OF ONE WORD REPLACEMENT.
    # * Eg.: {'*ot': ['hot', 'dot', 'lot'], ...}
    all_combinations = {}
    for word in wordList:
        for idx in range(beginWord_len):
            combo_word = f'{word[:idx]}*{word[idx + 1:]}'
            if combo_word not in all_combinations:
                all_combinations[combo_word] = []
            all_combinations[combo_word].append(word)
    # * -----------------------------------------------------------------------------------------------
    # * NOW USING BFS TO GO THROUGH ALL PATHS
    q = [(beginWord, 1)]
    visited = set(beginWord)

    while q:
        # * THIS IS A LEFT POP AS QUEUE IS FIFO
        cur_word, level = q.pop(0)

        # * NOW MAKEIGN THE SAME COMBO_WORD OF CUR_WORD AND GOING THROUGH ALL POSSIBLE WORDS
        for idx in range(beginWord_len):
            combo_word = f'{cur_word[:idx]}*{cur_word[idx + 1:]}'

            # * CHECKING IF THE COMBO_WORD IS IN THE ALL_COMBINATION LIST
            if combo_word in all_combinations:
                for next_word in all_combinations[combo_word]:
                    if next_word == endWord:

                        # * RETURINING +1 AS WE NEED TO TAKE ONE LAST JUMP
                        return level + 1
                    if next_word not in visited:
                        visited.add(next_word)
                        q.append((next_word, level + 1))
    return 0


print(ladderLength(beginWord="hit", endWord="cog",
                   wordList=["hot", "dot", "dog", "lot", "log", "cog"]))

print(ladderLength(beginWord="hit", endWord="cog",
                   wordList=["hot", "dot", "dog", "lot", "log"]))
