class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
      
        result=[]
        
        for i in range(0,len(nums)):
            count=0
            for j in nums:
                if nums[i]>j:
                 count+=1
            result.append(count)
        return result       
