class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums.sort()
        day = []
        while k>0:
            t=1
            maxx=0
            o=nums[0]
            phai=0
            for i in range(len(nums)-1):
                if nums[i] != nums[i+1]:
                    if maxx<t:
                        maxx = max(maxx,t)
                        o=nums[i]
                        phai=i
                    t=1
                else:
                    t+=1
            if maxx<t:
                maxx=t
                o=nums[-1]
                phai=len(nums)
            day.append(o)
            del nums[phai-maxx+1:phai+1]
            k-=1
        return day