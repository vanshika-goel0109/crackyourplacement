class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low=0
        high=len(nums)-1
        mid=0
        
        while(mid<=high):
            
            if(nums[mid]==0):
                nums[low],nums[mid]=nums[mid],nums[low]
                low+=1
                mid+=1
            elif(nums[mid]==2):
                nums[mid],nums[high]=nums[high],nums[mid]
                high-=1
            else:
                mid+=1
              
           
                

        return nums
