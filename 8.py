class solution:
    def myAtoi(self, s: str) -> int:
        n = len(s)
        i = 0
        result = 0
        sign = 1
        # Skip leading whitespaces
        while i < n and s[i] == ' ':
            i += 1
        if i == n:
            return 0
        # check for sign
        if s[i] == '-':
            sign = -1
            i += 1
        elif s[i] == '+':
            sign = 1
            i += 1
        # read continuous digits
        while i < n and s[i].isdigit():
            result = result * 10 + int(s[i])
            i += 1
        # Apply sign
        result = sign*result
        # Clamp the result to the 32-bit signed integer range
        if result < -2**31:
            return -2**31
        if result > 2**31 - 1:
            return 2**31 - 1
        return result
sol = solution()
s = "42"
print(sol.myAtoi(s))  # Output: -42