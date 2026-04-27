class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique = set()
        for i in nums:
            unique.add(i)

        if len(nums) == len(unique):
            return False
        else:
            return True


         