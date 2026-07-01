from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        pointer_from_end = len(height) - 1
        pointer_from_start = 0
        def get_area_by_two_pointer(pointer_from_start,pointer_from_end,height):
            height_of_walls = min(height[pointer_from_start], height[pointer_from_end])
            Width_of_the_two_walls = pointer_from_end - pointer_from_start
            area = height_of_walls * Width_of_the_two_walls
            return area
        def two_pointer_system(pointer_from_start,pointer_from_end,height):
            max_area = 0
            while(pointer_from_end > pointer_from_start):
                area = get_area_by_two_pointer(pointer_from_start,pointer_from_end,height)
                max_area = max(max_area, area)
                if height[pointer_from_start] < height[pointer_from_end]:
                    pointer_from_start+=1
                else:
                    pointer_from_end-=1
            return max_area
        max_area = two_pointer_system(pointer_from_start,pointer_from_end,height)
        return max_area