class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i,j=0,len(nums)-1
        while i<=j:
            max=(i+j)//2
            if nums[max]==target:
                return max
            elif nums[max] < target:
                i=max+1
            else:
                j=max-1
        return -1