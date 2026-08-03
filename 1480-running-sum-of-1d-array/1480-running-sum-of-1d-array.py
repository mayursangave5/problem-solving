class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        op=[]
        x=0
        for i in range(len(nums)):
            x=x+nums[i]
            op.append(x)
        return op