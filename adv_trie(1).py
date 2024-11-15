class AdvNode:
    def __init__(self, key=None):
        # IMPLEMENT YOUR OWN Trie Node.
        self._key = key
        self._children = dict()
        self.end_of_word = False 
        self.pass_through = 0
class AdvTrie:
    def __init__(self):
        # IMPLEMENT HERE
        self._root = AdvNode()
        self._num = 0 #for O(1) during __len__


    def insert(self, word: str) -> bool:
        """
        Inserts a word into the Trie.
        
        :param word: The word to be added to the Trie.
        :return: Boolean; True if the word was added, False if the word was already in the Trie.
        :complexity: O(L), where L is the length of the word.
        """
        # IMPLEMENT HERE
        current= self._root
        for letter in word:
            if letter not in current._children:
                current._children[letter] = AdvNode(letter)
                
            current = current._children[letter]
        if current.end_of_word == True:
            return False
        else:
            current.end_of_word = True
            self._num += 1
            return True
    
    def update_pass_through(self, word):
        if self.insert(word):
            current= self._root
            for letter in word:
                if letter in current._children:
                    current.pass_through += 1
                    current = current._children[letter]



    def search(self, word: str) -> bool:
        """
        Searches for a word in the Trie.
        
        :param word: The word to search in the Trie.
        :return: Boolean; True if the word exists in the Trie, False otherwise.
        :complexity: O(L), where L is the length of the word.
        """
        # IMPLEMENT HERE
        current= self._root
        for letter in word:
            if letter not in current._children:
                break 
            current = current._children[letter]
        if current.end_of_word == True:
            return True
        else:
            return False


    def starts_with(self, prefix: str) -> bool:
        """
        Checks if there is any word in the Trie that starts with the given prefix.
        
        :param prefix: The prefix to check in the Trie.
        :return: Boolean; True if any word in the Trie starts with the prefix, False otherwise.
        :complexity: O(L), where L is the length of the prefix.
        """
        # IMPLEMENT HERE
        scanall = 0
        current= self._root
        for letter in prefix:
            if letter not in current._children:
                break

            current = current._children[letter]
            scanall += 1
        if scanall == len(prefix):
            return True
        else:
            return False

        
    def __len__(self) -> int:
        """
        Returns the total number of words stored in the Trie.
        
        :return: Integer; the total count of words stored in the Trie.
        :complexity: O(1)
        """
        # IMPLEMENT HERE
        return self._num

    def remove(self, word: str) -> bool:
        """
        Removes a word from the Trie if it exists.
        
        :param word: The word to remove from the Trie.
        :return: Boolean True if the word was removed, False if the word was not found.
        :complexity: O(L), where L is the length of the word.
        """
        # IMPLEMENT HERE
        if not self.search(word):
            return False
        
        #the end letter is leaf
        current= self._root
        
        for letter in word[:-1]: 
            current = current._children[letter]
        if current._children == None:
            
            return True
        else:
            return False

        #the end letter is internal node
        


    def count_words_starting_with(self, prefix: str) -> int:
        """
        Counts words in the Trie that start with the given prefix.
        
        :param prefix: The prefix to count words for.
        :return: Integer count of words starting with the prefix.
        :complexity: O(L + M), where L is the length of the prefix and M is the number of child nodes under the prefix's last node.
        """
        # IMPLEMENT HERE


    def autocomplete(self, prefix: str) -> list:
        """
        Provides a list of all possible endings that can complete a given prefix to form a word in the Trie.
        
        :param prefix: The prefix to autocomplete.
        :return: List of strings; all completions of the given prefix that form words in the Trie.
        :complexity: O(L + N), where L is the length of the prefix and N is the number of characters in all autocomplete suggestions combined.
        """
        # IMPLEMENT HERE

    def longest_common_prefix(self) -> str:
        """
        Identifies and returns the longest common prefix shared by all keys in the Trie.
        
        :return: String; the longest common prefix shared by all words in the Trie.
        :complexity: O(minLen), where minLen is the length of the shortest word in the Trie.
        """
        # IMPLEMENT HERE

    def find_shortest_unique_prefix(self, word: str) -> str:
        """
        For a given word in the Trie, find the shortest prefix that uniquely identifies this word from all other words.
        
        :param word: The word to find the shortest unique prefix for.
        :return: String; the shortest unique prefix that identifies the given word from all other words in the Trie.
        :complexity: O(L), where L is the length of the word.
        """
        # IMPLEMENT HERE

    def wildcard_search(self, pattern: str) -> list:
        """
        Searches for words in the Trie that match a given pattern including wildcards.
        The '*' wildcard matches any sequence of characters (including an empty sequence),
        and '?' matches any single character.

        :param pattern: The pattern to search for, which may include '*' and '?' wildcards.
        :return: List of strings; all words in the Trie that match the given wildcard pattern.
        :complexity: O(P + K), where P is the length of the pattern and K is the number of matching words.

        Example:
        If the Trie contains 'apple', 'app', 'apricot', 'banana':
            wildcard_search('a*p') should return ['app', 'apple', 'apricot']
            wildcard_search('a??le') should return ['apple']
        """
        # IMPLEMENT HERE