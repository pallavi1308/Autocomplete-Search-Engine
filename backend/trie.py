class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True

    def starts_with(self, prefix):
        node = self.root
        results = []

        for ch in prefix:
            if ch not in node.children:
                return []
            node = node.children[ch]

        self._dfs(node, prefix, results)
        return results

    def _dfs(self, node, prefix, results):
        if len(results) >= 5:  # Limit to 5 suggestions
            return
        if node.is_end:
            results.append(prefix)
        for ch in node.children:
            self._dfs(node.children[ch], prefix + ch, results)
