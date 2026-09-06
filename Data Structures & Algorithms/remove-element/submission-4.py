class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        # remove val from nums
        # nums should be same array
            # brute make new array and append

        
        # arr_len= len(nums)
        # new_arr = [arr_len]

        # for i, num in enumerate(nums):
        #     if num == val:
        #         arr_len -= 1
        #     else:
        #         new_arr

        k = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        
        return k


        