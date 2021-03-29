# 首先放自己写的版本，竟然通过了。。。。用python的列表实现的，可是感觉没有用到 Trie树的概念。。。所以要看看其他人写的
# 自己的版本数据是：内存消耗 20.9M，超过96.49%，可是执行用时就比较慢了。

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = []


    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        self.trie.append(word)


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        if word in self.trie:
            return True
        return False


    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        for i in self.trie:
            if prefix == i[:len(prefix)]:
                return True
        return False



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)



# 来看看优秀的朋友们写的代码：

# 这才是 正宗的按照 Trie 树的定义来走。
class TrieNode:
# Initialize your data structure here.
def __init__(self):
    self.children = collections.defaultdict(TrieNode)
    self.is_word = False

class Trie:

def __init__(self):
    self.root = TrieNode()

def insert(self, word):
    current = self.root
    for letter in word:
        current = current.children[letter]
    current.is_word = True

def search(self, word):
    current = self.root
    for letter in word:
        current = current.children.get(letter)
        if current is None:
            return False
    return current.is_word

def startsWith(self, prefix):
    current = self.root
    for letter in prefix:
        current = current.children.get(letter)
        if current is None:
            return False
    return True
