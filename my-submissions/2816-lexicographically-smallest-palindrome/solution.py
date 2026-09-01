class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        left = 0
        right = len(s) - 1
        alphs = {
    'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 
    'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 
    'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 
    'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 
    'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26
}
        s_list = list(s)
        while left < right:
            if s_list[left] == s_list[right]:
                pass
            else:
                if alphs[s_list[left]] < alphs[s_list[right]]:
                    s_list[right] = s_list[left]
                else:
                    s_list[left] = s_list[right]
            left += 1
            right -= 1
        return ''.join(s_list)
