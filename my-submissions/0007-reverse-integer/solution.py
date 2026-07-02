class Solution:
    def reverse(self, x: int) -> int:
        -231 <= x <= 231 - 1
        char = str(x)
        chars = [i for i in char]
        new = []
        
        if x < 0:
            chars.pop(0)

        for i in range(len(chars)-1, -1, -1):
            new.append(chars[i])
        
        num = int(''.join(new))
        if x < 0:
            num = num * -1

        if -2**31 <= num <= 2**31 - 1:
            return num
        else:
            return 0



        
