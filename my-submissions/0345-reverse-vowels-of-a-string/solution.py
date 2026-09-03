class Solution:
    def reverseVowels(self, s: str) -> str:
        arr = []
        vowels = ['a','e','i','o','u','A','E','I','O','U']
        for i in s:
            arr.append(i)
        left = 0
        right = len(arr) - 1
        while left < right:
            if arr[left] not in vowels:
                left += 1
            elif arr[right] not in vowels:
                right -= 1
            elif arr[left] in vowels and arr[right] in vowels:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1
        return ''.join(arr)
