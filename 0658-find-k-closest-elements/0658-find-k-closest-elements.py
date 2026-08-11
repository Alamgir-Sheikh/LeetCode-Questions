class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        s = 0
        e = len(arr) - k
        while s < e:
            mid = s + (e - s) // 2
            if x - arr[mid] > arr[mid + k] - x:
                s = mid + 1
            else:
                e = mid
        return arr[s: s + k]
