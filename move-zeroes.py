approachh is to store the first index of zero in variable i and just next index into j, then swap if number at i==0 and number at j!=0, incrementing both i and j
else, you have to check next number so increment j in else case too.


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index=0
        for i in range(len(nums)):
            if nums[i]==0:
                index=i
                break
        i=index
        j=i+1
        
        while(j<len(nums)):
            if(nums[i]==0 and nums[j]!=0):
                nums[j],nums[i]=nums[i],nums[j]
                i+=1
                j+=1
            else:
                j+=1
        return nums
