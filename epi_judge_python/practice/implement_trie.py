class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # Use dict
        self.trie = {}

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        # Point cur to trie
        cur = self.trie
        # For each char, if not in trie, add dict for it in trie
        for char in word:
            if char not in cur:
                cur[char] = {}
            cur = cur[char]
        cur['*'] = True # '*' marks end of word


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        # Point cur to trie
        cur = self.trie
        # Check if each word char in trie
        for char in (word):
            if char not in cur:
                return False
            cur = cur[char]
        # After checking all word chars, check if at end of word
        if '*' not in cur:
            return False
        return True
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        # Point cur to trie
        cur = self.trie
        # Check if each prefix char in trie
        for char in (prefix):
            if char not in cur:
                return False
            cur = cur[char]
        return True


# Your Trie object will be instantiated and called as such:
trie = Trie()

trie.insert("apple")
print(trie.search("apple"))  # returns true
print(trie.search("app"))     # returns false
print(trie.startsWith("app")) # returns true
trie.insert("app")
print(trie.search("app"))     # returns true