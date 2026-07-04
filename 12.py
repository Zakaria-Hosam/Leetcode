class Solution:
    def intToRoman(self, num: int) -> str:
        def get_roman_numerals(num):
            thousands = num // 1000
            hundreds = (num % 1000) // 100
            tens = (num % 100) // 10
            ones = num % 10
            roman_numerals = {
                1: 'I',
                5: 'V',
                10: 'X',
                50: 'L',
                100: 'C',
                500: 'D',
                1000: 'M'
            }
            roman_string = ''
            if thousands > 0 and thousands < 4:
                roman_string += roman_numerals[1000] * thousands
            #multiplies of hundred
            if hundreds > 0 and hundreds < 4:
                roman_string += roman_numerals[100] * hundreds
            elif hundreds == 4:
                roman_string += 'CD'
            elif hundreds == 5:
                roman_string += 'D'
            elif hundreds > 5 and hundreds < 9:
                roman_string += 'D' + roman_numerals[100] * (hundreds - 5)
            elif hundreds == 9:
                roman_string += 'CM'
            #multiplies of ten
            if tens > 0 and tens < 4:
                roman_string += roman_numerals[10] * tens
            elif tens == 4:
                roman_string += 'XL'
            elif tens == 5:
                roman_string += 'L'
            elif tens > 5 and tens < 9:
                roman_string += 'L' + roman_numerals[10] * (tens - 5)
            elif tens == 9:
                roman_string += 'XC'
            #Multiplies of one
            if ones > 0 and ones < 4:
                roman_string += roman_numerals[1] * ones
            elif ones == 4:
                roman_string += 'IV'
            elif ones == 5:
                roman_string += 'V'
            elif ones > 5 and ones < 9:
                roman_string += 'V' + roman_numerals[1] * (ones - 5)
            elif ones == 9:
                roman_string += 'IX'
            return roman_string
        roman_string = get_roman_numerals(num)
        return roman_string