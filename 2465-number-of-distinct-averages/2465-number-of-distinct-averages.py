class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        distinct_avg = []
        nums.sort()
        low = 0
        high = len(nums) - 1

        while low <= high:
            avg = (nums[low] + nums[high]) / 2
            if avg not in distinct_avg:
                distinct_avg.append(avg)
            low += 1
            high -= 1
            
        return len(distinct_avg)