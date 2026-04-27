class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #brute force is to cycle through each possible

        for i in range(len(nums)):
            for j in range(len(nums) + 1):
                if j < len(nums) and nums[i] + nums[j] == target and i != j:
                    return [i, j]

        