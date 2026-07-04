class Solution:
    def intToRoman(self, num: int) -> str:
        def checks(num):
            multiplies_of_thousand = num // 1000
            multiplies_of_hundred = (num % 1000) // 100
            multiplies_of_ten = (num % 100) // 10
            multiplies_of_one = num % 10
            return multiplies_of_thousand, multiplies_of_hundred, multiplies_of_ten, multiplies_of_one
        multiplies_of_thousand, multiplies_of_hundred, multiplies_of_ten, multiplies_of_one = checks(num)
        roman_numerals = {
            1: 'I',
            5: 'V',
            10: 'X',
            50: 'L',
            100: 'C',
            500: 'D',
            1000: 'M'
        }
        multiplies_of_thousand, multiplies_of_hundred, multiplies_of_ten, multiplies_of_one = checks(num)
        def get_roman_numerals(multiplies_of_thousand, multiplies_of_hundred, multiplies_of_ten, multiplies_of_one):
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
            if multiplies_of_thousand > 0 and multiplies_of_thousand < 4:
                roman_string += roman_numerals[1000] * multiplies_of_thousand
            #multiplies of hundred
            if multiplies_of_hundred > 0 and multiplies_of_hundred < 4:
                roman_string += roman_numerals[100] * multiplies_of_hundred
            elif multiplies_of_hundred == 4:
                roman_string += 'CD'
            elif multiplies_of_hundred == 5:
                roman_string += 'D'
            elif multiplies_of_hundred > 5 and multiplies_of_hundred < 9:
                roman_string += 'D' + roman_numerals[100] * (multiplies_of_hundred - 5)
            elif multiplies_of_hundred == 9:
                roman_string += 'CM'
            #multiplies of ten
            if multiplies_of_ten > 0 and multiplies_of_ten < 4:
                roman_string += roman_numerals[10] * multiplies_of_ten
            elif multiplies_of_ten == 4:
                roman_string += 'XL'
            elif multiplies_of_ten == 5:
                roman_string += 'L'
            elif multiplies_of_ten > 5 and multiplies_of_ten < 9:
                roman_string += 'L' + roman_numerals[10] * (multiplies_of_ten - 5)
            elif multiplies_of_ten == 9:
                roman_string += 'XC'
            #Multiplies of one
            if multiplies_of_one > 0 and multiplies_of_one < 4:
                roman_string += roman_numerals[1] * multiplies_of_one
            elif multiplies_of_one == 4:
                roman_string += 'IV'
            elif multiplies_of_one == 5:
                roman_string += 'V'
            elif multiplies_of_one > 5 and multiplies_of_one < 9:
                roman_string += 'V' + roman_numerals[1] * (multiplies_of_one - 5)
            elif multiplies_of_one == 9:
                roman_string += 'IX'
            return roman_string
        roman_string = get_roman_numerals(multiplies_of_thousand, multiplies_of_hundred, multiplies_of_ten, multiplies_of_one)
        return roman_string