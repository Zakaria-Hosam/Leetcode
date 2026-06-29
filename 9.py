class Solution:
    def isPalindrome(self, x: int) -> bool:
        max_int = 2**31 - 1
        min_int = -2**31
        if x > max_int or x < min_int:
            return False
        if x < 0:
            return False
        str_x = str(x)
        if str_x == str_x[::-1]:
            return True
        else:
            return False