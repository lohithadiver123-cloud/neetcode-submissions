import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        heap=[]
        for num in nums:
            if num in freq:
                freq[num]+=1
            else :
                freq[num]=1
        for key ,value in freq.items():
            if len(heap)<k:
                heapq.heappush(heap,(value,key))
            else:
                heapq.heappushpop(heap,(value,key))
        return [item[1] for item in heap]       

        
        