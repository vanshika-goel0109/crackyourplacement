class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for num in nums:
            ind = abs(num)
            
            if nums[ind] < 0:
                return ind
            
            nums[ind] *= -1 


       
