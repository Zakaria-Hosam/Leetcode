from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        def get_indexes_for_height(height):
            indices = {}
            for i in range(len(height)):
                    indices[i] = height[i]
            return indices
        indices = get_indexes_for_height(height)
        def get_shorter_index(i,j,height):
            return min(height[i],height[j])
        def get_max_area(indices,height):
            areas = []
            keys = sorted(indices.keys())
            for i in range(len(keys)):
                for j in range(i+1,len(keys)):
                        width_of_one = abs(keys[i]-keys[j])
                        height_of_one = get_shorter_index(keys[i],keys[j],height)
                        area = width_of_one * height_of_one
                        areas.append(area)
            return areas
        areas = get_max_area(indices,height)
        max_area = max(areas)
        return max_area