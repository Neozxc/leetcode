class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        count = 0
        n = len(arr)
        
        for j in range(1, n - 1):
            i = 0
            k = j + 1
            
            valid_i_count = 0

            for i in range(j):
                if abs(arr[i] - arr[j]) <= a:
                    valid_i_count += 1
            
            if valid_i_count == 0:
                continue
                
            valid_k_count = 0

            for k in range(j + 1, n):
                if abs(arr[j] - arr[k]) <= b:
                    valid_k_count += 1
                    for i in range(j):
                        if abs(arr[i] - arr[j]) <= a and abs(arr[i] - arr[k]) <= c:
                            count += 1
        
        return count
