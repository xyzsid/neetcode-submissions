class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        # set and then add to that set
        # if we can't add to a set then return true
        # else return false

        s = set(nums)

        return len(nums) != len(s)

        # if s.len() != nums.len()

        # for num in nums:
        #     if num in s:
        #         return True
        
        # return False