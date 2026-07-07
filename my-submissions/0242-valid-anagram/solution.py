class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        an1 = {}
        an2 = {}
        for i in s:
            if i in an1:
                an1[i] = an1[i] + 1
            else:
                an1[i] = 1
        for i in t:
            if i in an2:
                an2[i] = an2[i] + 1
            else:
                an2[i] = 1

        if an1 == an2:
            return True
        else:
            return False
            
