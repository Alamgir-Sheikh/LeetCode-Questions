class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        averages = []
        nums.sort()
        low = 0
        high = len(nums) - 1

        while low <= high:
            avg = (nums[low] + nums[high]) / 2
            averages.append(avg)
            low += 1
            high -= 1
        
        return min(averages)