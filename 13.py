class Solution:
    def romanToInt(self, s: str) -> int:
        roman_numerals = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        def roman_to_intger(string):
            length = len(string)
            total = 0
            i = 0
            while(i < length):
                try:
                    if roman_numerals[string[i]] >= roman_numerals[string[i+1]]:
                        total = total + roman_numerals[string[i]]
                        i = i + 1
                    elif roman_numerals[string[i]] < roman_numerals[string[i+1]]:
                        total = total + abs((roman_numerals[string[i]] - roman_numerals[string[i+1]]))
                        i = i + 2
                except:
                    total = total + roman_numerals[string[i]]
                    break
            return total
        return roman_to_intger(s)
