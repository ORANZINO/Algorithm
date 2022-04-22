from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.order = 0
        self.count = 0
        self.word = False
        self.children = defaultdict(TrieNode)


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for i, char in enumerate(word, start=1):
            node.children[char].order = i
            node.children[char].count += 1
            node = node.children[char]
        node.word = True


def solution(words):
    trie = Trie()
    answer = 0

    for word in words:
        trie.insert(word)

    stack = list(trie.root.children.values())

    while stack:
        node = stack.pop()
        if node.count > 1:
            if node.word:
                answer += node.order
            for child in node.children:
                stack.append(node.children[child])
        else:
            answer += node.order

    return answer

