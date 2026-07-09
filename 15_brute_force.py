class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        array = nums
        array.sort()

        seen = set()
        possible_combination = []
        found_combination = []
        loged = []

        for i in range(len(array)):
            possible_combination.append(-1 * array[i])

        for i in range(len(array)):
            sum = possible_combination[i]

            for j in range(len(array)):
                for k in range(len(array)):
                    target = array[j] + array[k]

                    if target == sum and j != i and i != k and k != j:
                        possible_one_combination = [array[i], array[j], array[k]]
                        possible_one_combination.sort()

                        key = tuple(possible_one_combination)

                        if key not in seen:
                            found_combination.append(possible_one_combination)
                            seen.add(key)

        return found_combination