class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        dct = {}
        for i in s:
            if i not in dct:
                dct[i] = 1
            else:
                dct[i] += 1
        for i in t:
            if i in dct:
                dct[i] -= 1
            else:
                return i
        for i in dct:
            if dct[i] == -1:
                return i
