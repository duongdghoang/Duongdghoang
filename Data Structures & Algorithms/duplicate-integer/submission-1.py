class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        trung = set()
        for num in nums:
            if num in trung:
                return True
            trung.add(num)
        return False
