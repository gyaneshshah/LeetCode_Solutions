class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        firstrow = 'q w e r t y u i o p Q W E R T Y U I O P'
        secondrow = 'a s d f g h j k l A S D F G H J K L'
        thirdrow = 'z x c v b n m Z X C V B N M'
        firstarray = firstrow.split()
        secondarray = secondrow.split()
        thirdarray = thirdrow.split()
        ans = []
        for word in words:
            if word[0] in firstarray:
                check = firstarray
            elif word[0] in secondarray:
                check = secondarray
            else:
                check = thirdarray
            cnt = 1
            for letters in word:
                if letters not in check:
                    cnt = 0
                    break
            if cnt == 1:
                ans.append(word)
        return ans
