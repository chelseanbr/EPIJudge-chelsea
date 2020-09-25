class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # Use dict
        self.trie = {}
        self.cur = self.trie

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        # Point cur to trie
        self.cur = self.trie
        # For each char, if not in trie, add dict for it in trie
        for char in word:
            if char not in self.cur:
                self.cur[char] = {}
            self.cur = self.cur[char]
        self.cur['*'] = True # '*' marks end of word


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        if self.searchPrefix(word) and '*' in self.cur:
            return True
        else: 
            return False
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        return self.searchPrefix(prefix)

    def searchPrefix(self, string):
        # Point cur to trie
        self.cur = self.trie
        # Check if each string char in trie
        for char in (string):
            if char not in self.cur:
                return False
            self.cur = self.cur[char]
        return True

# Your Trie object will be instantiated and called as such:
trie = Trie()

trie.insert("apple")
print(trie.search("apple"))  # returns true
print(trie.search("app"))     # returns false
print(trie.startsWith("app")) # returns true
trie.insert("app")
print(trie.search("app"))     # returns true