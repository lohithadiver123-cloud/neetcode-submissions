class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm ={}
        n=len(nums)
        for i in range (0,n):
            comp=target-nums[i]
            if comp in hm:
                return [hm[comp],i]
            hm[nums[i]]=i   
           
            
