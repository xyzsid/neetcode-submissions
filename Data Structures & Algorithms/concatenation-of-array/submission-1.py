class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # ans = nums + nums

        # return ans

        ans = list(nums)

        for num in nums:
            ans.append(num)

        return ans