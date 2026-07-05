class Solution:
    def intToRoman(self, num: int) -> str:

        def convert_to_string(num):
            num = str(num)

            if len(num) < 4:
                num = num.zfill(4)

            list_of_numbers = []

            for i in range(len(num)):
                list_of_numbers.append(num[i])

            return list_of_numbers

        def get_roman_numerals(num):
            string_to_convert = convert_to_string(num)
            roman_string = ""

            roman = {
                1: ("I", 0),
                5: ("V", 1),
                10: ("X", 1),
                50: ("L", 10),
                100: ("C", 10),
                500: ("D", 100),
                1000: ("M", 100)
            }

            lengths = {
                3: 1,
                2: 10,
                1: 100,
                0: 1000
            }

            for i in range(len(string_to_convert)):

                if string_to_convert[i] == '0':
                    continue

                elif string_to_convert[i] == '4' or string_to_convert[i] == '9':
                    index = (int(string_to_convert[i]) + 1) * lengths[i]
                    roman_string = roman_string + roman[roman[index][1]][0] + roman[index][0]

                elif string_to_convert[i] == '5':
                    index = int(string_to_convert[i]) * lengths[i]
                    roman_string = roman_string + roman[index][0]

                elif int(string_to_convert[i]) > 5:
                    index_of_the_five_subtraction = int(string_to_convert[i]) - 5
                    roman_string = roman_string + (
                        roman[5 * lengths[i]][0]
                        + index_of_the_five_subtraction * roman[1 * lengths[i]][0]
                    )

                else:
                    index = int(string_to_convert[i])
                    roman_string = roman_string + index * roman[1 * lengths[i]][0]

            return roman_string

        return get_roman_numerals(num)