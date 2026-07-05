class Solution:
    def merge(self, left_arr, right_arr):
        res = []
        i = 0
        j = 0
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                res.append(left_arr[i])
                i += 1
            else:
                res.append(right_arr[j])
                j += 1
        while i < len(left_arr):
            res.append(left_arr[i])
            i += 1
        while j < len(right_arr):
            res.append(right_arr[j])
            j += 1
        return res

    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        # Divide
        mid = (len(nums)) // 2
        left_arr = nums[:mid]
        right_arr = nums[mid:]
        sorted_left = self.sortArray(left_arr)
        sorted_right = self.sortArray(right_arr)

        return self.merge(sorted_left, sorted_right)
        
        