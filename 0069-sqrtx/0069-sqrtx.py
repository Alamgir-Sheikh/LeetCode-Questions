class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x
            
        low, high = 1, x
        ans = 0
        
        while low <= high:
            mid = (low + high) // 2
            
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                low = mid + 1
                ans = mid  # Keep track of the closest smaller floor
            else:
                high = mid - 1
                
        return ans