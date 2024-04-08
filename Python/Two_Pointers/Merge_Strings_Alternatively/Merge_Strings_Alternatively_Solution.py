class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i=0
        ans_s = ""
        word1_len = len(word1)
        word2_len = len(word2)
        while i<word1_len and i<word2_len:
            ans_s += word1[i] + word2[i]
            i+=1

        if word1_len>word2_len:
            ans_s += word1[i:word1_len]
        elif word2_len>word1_len:
            ans_s += word2[i:word2_len]
        return ans_s
