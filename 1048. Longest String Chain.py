from typing import List
import collections

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        # Group the word by length, in each iteration, take two consectuive array, determine of this word can be extend
        words_extension = {w: 1 for w in words} # stores word: longest length of the word chain ends at that word
        length_word = collections.defaultdict(list)
        for w in words:
            length_word[len(w)].append(w)
        sorted_by_length = sorted(length_word.items())
        for i in range(len(sorted_by_length)):
            self._can_extend_group(words_extension, sorted_by_length, length_word, i)
        return max(words_extension.values())
    
    def _can_extend_group(self, words_extension, sorted_by_length, length_word, current_index):
        current = sorted_by_length[current_index]
        if current[0] - 1 in length_word:
            prev = length_word[current[0] - 1]
            for curr_word in current[1]:
                for prev_word in prev:
                    if self._can_extend(prev_word, curr_word):
                        words_extension[curr_word] = max(words_extension[curr_word], words_extension[prev_word] + 1)
    
    
    def _can_extend(self, word1: str, word2: str) -> bool:
        word1_index = {w: i for i, w in enumerate(word1)}
        word2_index = {w: i for i, w in enumerate(word2)}
        for k in word1_index:
            if k not in word2_index:
                return False
            if word2_index[k] != word1_index[k] and word2_index[k] - 1 != word1_index[k]:
                return False
        return True
        
if __name__ == '__main__':
    sol = Solution()
    words = ["qyssedya","pabouk","mjwdrbqwp","vylodpmwp","nfyqeowa","pu","paboukc","qssedya","lopmw","nfyqowa","vlodpmw","mwdrqwp","opmw","qsda","neo","qyssedhyac","pmw","lodpmw","mjwdrqwp","eo","nfqwa","pabuk","nfyqwa","qssdya","qsdya","qyssedhya","pabu","nqwa","pabqoukc","pbu","mw","vlodpmwp","x","xr"]
    print(sol.longestStrChain(words))