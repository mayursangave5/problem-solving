class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        list=[]
        mod=0
        for x in nums:
            mod=(mod*2+x)%5
            list.append(mod==0)  
        return list
        