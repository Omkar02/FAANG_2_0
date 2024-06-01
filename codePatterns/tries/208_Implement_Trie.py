class Trie:
    def __init__(self) -> None:
        self.trie = {}
        self.end_word = '*'

    def insert(self, word: str) -> None:
        cur_node = self.trie
        for w in word:
            if w not in cur_node:
                cur_node[w] = {}
            cur_node = cur_node[w]
        cur_node[self.end_word] = word
        return self

    def search(self, word: str) -> bool:
        cur_node = self.trie
        for w in word:
            if w in cur_node:
                cur_node = cur_node[w]
            else:
                return False
        return True if self.end_word in cur_node and cur_node[self.end_word] == word else False

    def startsWith(self, prefix: str) -> bool:
        cur_node = self.trie
        for pre in prefix:
            if pre not in cur_node:
                return False
            cur_node = cur_node[pre]
        return True

    def printTrie(self):
        print(self.trie)
        return self


t: Trie = Trie().insert("apple")
print(t.search("apple"))
print(t.search("applea"))
print(t.startsWith("app"))
