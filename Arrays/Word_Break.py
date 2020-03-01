# Word - Break : Leetcode - 139

class Solution:
    def wordBreak(self, s:str, wordDict):

        wordSet = set(wordDict)
        a = [False] * (len(s) + 1)
        a[0] = True
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                if s[i:j] in wordSet and a[i] == True:
                    a[j] = True
        return a[-1]
