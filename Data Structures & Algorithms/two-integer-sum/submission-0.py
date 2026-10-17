class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        day = {}
        for i in range(len(nums)):
            tru = target - nums[i]
            if tru in day:
                return [day[tru],i]
            day[nums[i]] = i
    

