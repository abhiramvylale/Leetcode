class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        arr = []
        for i in s:
            arr.append(i)
        l = 0
        r = len(arr) - 1
        while l < r:
            if arr[l].isalpha() and arr[r].isalpha():
                arr[l], arr[r] = arr[r], arr[l]
                l += 1
                r -= 1
            elif arr[l].isalpha():
                r -= 1
            elif arr[r].isalpha():
                l += 1
            else:
                l += 1
                r -= 1

        return ''.join(arr)
