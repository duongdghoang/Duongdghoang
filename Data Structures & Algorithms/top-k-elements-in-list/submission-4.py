class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        day=[]
        for n in nums:
            if n not in count:
                count[n]=0
            count[n]+=1
        while k>0:
            maxx=max(count, key=count.get)
            day.append(maxx)
            del count[maxx]
            k-=1
        return day
