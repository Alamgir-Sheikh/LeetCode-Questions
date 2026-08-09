class Solution:
    def findMin(self, nums: List[int]) -> int:
        s = 0
        e = len(nums) - 1
        mid = s + (e - s) // 2
        while s < e:
            if nums[mid] > nums[e]:
                s = mid + 1
            else:
                e = mid
            mid = s + (e - s) // 2
        return nums[s]