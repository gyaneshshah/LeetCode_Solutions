class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        for i, char in enumerate(word):
            if char==ch:
                return word[i::-1] + word[i+1:]
        return word
