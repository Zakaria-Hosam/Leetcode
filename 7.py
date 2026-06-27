class Solution:
    def reverse(self, x: int) -> int:
        min_int = -2**31
        max_int = (2**31) - 1
        if x >= 0:
            rev = str(x)
            intger_reversed = rev[::-1]
            returned = int(intger_reversed)
        else:
            x = x*-1
            rev = str(x)
            intger_reversed = rev[::-1]
            returned = -1 * int(intger_reversed)
        if returned>max_int or returned<min_int:
            returned  = 0
        return returned
        