class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        
        def count_le(val: int) -> int:
            count = 0
            for n1 in nums1:
                if n1 > 0:
                    target = val // n1
                    count += bisect.bisect_right(nums2, target)
                elif n1 < 0:
                    target = -(val // -n1)
                    idx = bisect.bisect_left(nums2, target)
                    count += len(nums2) - idx
                else:
                    if val >= 0:
                        count += len(nums2)
            return count

        low = -10**10 - 1
        high = 10**10 + 1
        ans = -1

        while low <= high:
            mid = (low + high) // 2
            
            if count_le(mid) >= k:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
                
        return ans
