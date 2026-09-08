class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # sorts = sorted(nums)
        # quantity = 0
        # num = sorts[0]

        # print(sorts)

        # for sort in sorts:
        #     if sort == num:
        #         quantity += 1
        
        # if quantity >= num / 2:
        #     return num
        

        counter = {}
        max_count = 0
        result = 0

        for num in nums:
            if num not in counter:
                counter[num] = 1
            else:
                counter[num] += 1

        for num, count in counter.items():
            if count > max_count:
                max_count = count
                result = num

        return result
