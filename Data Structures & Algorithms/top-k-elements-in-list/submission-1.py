import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        n=len(nums)
        for num in nums:
            if num in freq:
                freq[num]+=1
            else :
                freq[num]=1
        bucket=[[] for _ in range(n+1)]
        for key , value in freq.items():
                bucket[value].append(key)
        ret=[]
        for i in range(n,-1,-1):
            for num in bucket[i]:
                if len(ret)< k:
                    ret.append(num)

        return ret            



        
        