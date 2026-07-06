class Solution:
    def reverseWords(self, s: str) -> str:
        s.strip()
        words = [word for word in s.split()]
        result = []
        for i in range((len(words)-1), -1, -1):
            result.append(words[i])

        return ' '.join(result)

