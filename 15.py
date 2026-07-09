class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        array = nums
        array.sort()

        seen = set()
        found_combination = []

        def two_pointer_system(pivot, array):
            pointer_1 = pivot + 1
            pointer_2 = len(array) - 1
            target = -1 * (array[pivot])

            while pointer_2 > pointer_1:
                check = array[pointer_1] + array[pointer_2]

                if check == target:
                    found = [array[pointer_1], array[pointer_2], array[pivot]]
                    found.sort()
                    key = tuple(found)

                    if key not in seen:
                        found_combination.append(found)
                        seen.add(key)
                        pointer_1 += 1
                        pointer_2 -=1
                    else:
                        pointer_1 += 1
                        pointer_2 -= 1
                elif target < check:
                    pointer_2 -= 1

                elif target > check:
                    pointer_1 += 1

        for i in range(len(array)):
            two_pointer_system(i, array)

        return found_combination