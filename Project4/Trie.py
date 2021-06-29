"""
Chengming Wang
Project 4 - Tries
CSE 331 Fall 2020
Professor Sebnem Onsay
"""

from __future__ import annotations
from typing import Tuple, Dict, List
import string


class TrieNode:
    """
    Implementation of a trie node.
    """

    # DO NOT MODIFY

    __slots__ = "children", "is_end"

    def __init__(self, arr_size: int = 26) -> None:
        """
        Constructs a TrieNode with arr_size slots for child nodes.
        :param arr_size: Number of slots to allocate for child nodes.
        :return: None
        """
        self.children = [None] * arr_size
        self.is_end = 0

    def __str__(self) -> str:
        """
        Represents a TrieNode as a string.
        :return: String representation of a TrieNode.
        """
        if self.empty():
            return "..."
        children = self.children  # to shorten proceeding line
        return str(
            {chr(i + ord("a")) + "*" * min(children[i].is_end, 1): children[i] for i in range(26) if children[i]})

    def __repr__(self) -> str:
        """
        Represents a TrieNode as a string.
        :return: String representation of a TrieNode.
        """
        return self.__str__()

    def __eq__(self, other: TrieNode) -> bool:
        """
        Compares two TrieNodes for equality.
        :return: True if two TrieNodes are equal, else False
        """
        if not other or self.is_end != other.is_end:
            return False
        return self.children == other.children

    # Implement Below

    def empty(self) -> bool:
        """
        checks if the node is a leaf
        :return: Return true if node has no children.
        """
        return not any(self.children)

    @staticmethod
    def _get_index(char: str) -> int:
        """
        Returns the integer index of a character in a-z or A-Z. Should convert character to lowercase
        :param char: character to be mapped to integer.
        :return: Return integer index (0-25) of a character in a-z or A-Z.
        """
        return string.ascii_letters.index(char) % 26

    def get_child(self, char: str) -> TrieNode:
        """
        get the character child of the TrieNode with value char
        :param char: child character.
        :return: Return the child TrieNode with character index.
        """
        return self.children[TrieNode._get_index(char)]

    def set_child(self, char: str) -> None:
        """
        sets the child character TrieNode at the index of the character in its children`
        :param char: child character
        :return: None.
        """
        charNode = self.children[TrieNode._get_index(char)]
        if charNode is None:
            self.children[TrieNode._get_index(char)] = TrieNode()

    def delete_child(self, char: str) -> None:
        """
        deletes the child character TrieNode at the index of the character in its children
        :param char: the child character.
        :return: None.
        """
        self.children[TrieNode._get_index(char)] = None


class Trie:
    """
    Implementation of a trie.
    """

    # DO NOT MODIFY

    __slots__ = "root", "unique", "size"

    def __init__(self) -> None:
        """
        Constructs an empty Trie.
        :return: None.
        """
        self.root = TrieNode()
        self.unique = 0
        self.size = 0

    def __str__(self) -> str:
        """
        Represents a Trie as a string.
        :return: String representation of a Trie.
        """
        return "Trie Visual:\n" + str(self.root)

    def __repr__(self) -> str:
        """
        Represents a Trie as a string.
        :return: String representation of a Trie.
        """
        return self.__str__()

    def __eq__(self, other: Trie) -> bool:
        """
        Compares two Tries for equality.
        :return: True if two Tries are equal, else False
        """
        return self.root == other.root

    # Implement Below

    def add(self, word: str) -> int:
        """
        adds a word to the trie by traversing from root and storing characters from word one by one
        :param word: word to be added.
        :return: number of times word exists in trie.
        """
        def add_inner(node: TrieNode, index: int) -> int:
            node.set_child(word[index])
            child = node.get_child(word[index])
            if index == len(word) - 1:
                child.is_end += 1
                return child.is_end
            char = child
            return add_inner(char, index + 1)

        if word is None or not word or not word.isascii():
            return 0
        self.size += 1
        count = add_inner(self.root, 0)
        if count == 1:
            self.unique += 1
        return count

    def search(self, word: str) -> int:
        """
        searches the word in the trie and returns the number of times word has been added to trie.
        :param word: word to be searched.
        :return: number of times word exists in trie.
        """

        def search_inner(node: TrieNode, index: int) -> int:
            child = node.get_child(word[index])
            if child is None:
                return 0
            if index == len(word) - 1:
                return child.is_end
            return search_inner(child, index + 1)
        if word is None or not word or not word.isascii():
            return 0
        result = search_inner(self.root, 0)
        return result

    def delete(self, word: str) -> int:
        """
        Deletes the word from the trie
        :param word: word to be deleted.
        :return: Returns 0 if word is not found in Trie, else returns the number of times
        word existed in trie before deletion.
        """

        def delete_inner(node: TrieNode, index: int) -> Tuple[int, bool]:
            child = node.get_child(word[index])
            if child is None:
                return 0, False
            if index == len(word) - 1:
                actual_count = child.is_end
                child.is_end = 0
                can_prune = False
                if actual_count != 0 and child.empty():
                    can_prune = True
                return actual_count, can_prune
            nodes_deleted, can_delete = delete_inner(child, index + 1)
            if can_delete:
                child.delete_child(word[index+1])
            return nodes_deleted, child.is_end == 0 and child.empty()
        if word is None or not word or not word.isascii():
            return 0
        result, can_delete = delete_inner(self.root, 0)
        if can_delete:
            self.root.delete_child(word[0])
        if result != 0:
            self.size -= result
            self.unique -= 1
        return result

    def __len__(self) -> int:
        """
        Returns the size of the trie which is all the words in the trie.
        :return: Return the size of the trie.
        """
        return self.size

    def __contains__(self, word: str) -> bool:
        """
        checks if a word exists in the trie.
        :param word: word to be checked.
        :return: true if the word exists, false otherwise.
        """
        return self.search(word) != 0

    def empty(self) -> bool:
        """
        checks if the trie is empty.
        :return: true if there are no words in trie, false otherwise.
        """
        return self.size == 0

    def get_vocabulary(self, prefix: str = "") -> Dict[str, int]:
        """
        Returns a dictionary of (word, count) pairs containing every word in the `Trie` beginning with `prefix`.
        :param prefix: the prefix to be searched.
        :return: returns the dictionary of word count mapping for words starting with prefix.
        """

        def get_vocabulary_inner(node, suffix):
            if node.is_end > 0:
                vocab_dict[prefix+suffix] = node.is_end
            if node.empty():
                return
            for index, child in enumerate(node.children):
                if child is not None:
                    get_vocabulary_inner(child, suffix + string.ascii_letters[index])
        vocab_dict = {}
        start = self.root
        for char in prefix:
            if start is not None:
                start = start.get_child(char)
            else:
                return {}
        if start is not None:
            get_vocabulary_inner(start, "")
        return vocab_dict

    def autocomplete(self, word: str) -> Dict[str, int]:
        """
        Returns a dictionary of `(word, count)` pairs containing every word in the `Trie`
        which matches the template of `word`, where periods (.) in `word` may be filled
        with any character.
        :param word: template word.
        :return: dictionary of `(word, count)` pairs which matches the template.
        """

        def autocomplete_inner(node, prefix, index):
            if node is None:
                return
            if index == len(word)-1:
                if word[index] != ".":
                    child = node.get_child(word[index])
                    if child is not None and child.is_end > 0:
                        vocab_dict[prefix+word[index]] = child.is_end
                else:
                    for index, child in enumerate(node.children):
                        if child is not None and child.is_end > 0:
                            vocab_dict[prefix+string.ascii_letters[index]] = child.is_end
                return
            if word[index] != ".":
                child = node.get_child(word[index])
                if child is not None:
                    autocomplete_inner(child, prefix + word[index], index+1)
            else:
                for idx, child in enumerate(node.children):
                    if child is not None:
                        autocomplete_inner(child, prefix + string.ascii_letters[idx], index+1)

        vocab_dict = {}
        autocomplete_inner(self.root, "", 0)
        return vocab_dict


class TrieClassifier:
    """
    Implementation of a trie-based text classifier.
    """

    # DO NOT MODIFY

    __slots__ = "tries"

    def __init__(self, classes: List[str]) -> None:
        """
        Constructs a TrieClassifier with specified classes.
        :param classes: List of possible class labels of training and testing data.
        :return: None.
        """
        self.tries = {}
        for cls in classes:
            self.tries[cls] = Trie()

    @staticmethod
    def accuracy(labels: List[str], predictions: List[str]) -> float:
        """
        Computes the proportion of predictions that match labels.
        :param labels: List of strings corresponding to correct class labels.
        :param predictions: List of strings corresponding to predicted class labels.
        :return: Float proportion of correct labels.
        """
        correct = sum([1 if label == prediction else 0 for label, prediction in zip(labels, predictions)])
        return correct / len(labels)

    # Implement Below

    def fit(self, class_strings: Dict[str, List[str]]) -> None:
        """
        Train the classifier with predefined classes of sentences.
        :param class_strings:  A dictionary of `(class, List[str])` pairs to
        train the classifier on. Each string (tweet) in the list of strings
        associated to a class consists of multiple words.
        :return: None
        eturn value here.
        """
        for key in class_strings:
            for tweet in class_strings[key]:
                tweetwords = [item.strip() for item in tweet.split(" ")]
                for tweetWord in tweetwords:
                    self.tries[key].add(tweetWord)

    def predict(self, strings: List[str]) -> List[str]:
        """
        Predicts the class of a string (tweet) by splitting the string
        into individual words and Creating a class score for each
        string (tweet)
        :param strings: A list of strings (tweets) to be classified.
        :return: Returns a list of predicted classes corresponding to the input strings.
        """
        results = []
        for tweet in strings:
            class_scores = {}
            for token in tweet.split(" "):
                for key in self.tries:
                    is_end = self.tries[key].search(token)
                    class_scores[key] = class_scores.get(key, 0) + is_end
            max_score = 0
            max_class = ''
            for c in class_scores:
                class_scores[c] = class_scores[c] / self.tries[c].__len__()
                if class_scores[c] > max_score:
                    max_score = class_scores[c]
                    max_class = c
            results.append(max_class)
        return results






