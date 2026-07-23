class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        s = 0
        e = len(height) - 1

        while s < e:
            if height[s] < height[e]:
                area = height[s] * (e - s)
                max_area = max(max_area, area)
                s += 1
            else:
                area = height[e] * (e - s)
                max_area = max(max_area, area)
                e -= 1
        return max_area