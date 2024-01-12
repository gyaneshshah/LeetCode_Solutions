class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        #Initialising a new array equal to nums
        arr=nums
        flag=1
        #Running a while loop to remove val from arr completely
        while flag==1:
            if val in arr:
                arr.remove(val)
            else:
                flag=0
        nums=arr
        return len(nums)
