class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # brute force
        # we would just 

        new_arr = []

        for num in nums:
            if num not in new_arr:
                new_arr.append(num)
            else:
                return True

        return False
        
        
        