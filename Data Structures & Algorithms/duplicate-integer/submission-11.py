class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        # set and then add to that set
        # if we can't add to a set then return true
        # else return false

        # brute force is where we iterate through array

        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] == nums[j]:
        #             return True

        # return False

        s = set(nums)

        return len(nums) != len(s)

        # if s.len() != nums.len()

        # for num in nums:
        #     if num in s:
        #         return True
        
        # return False