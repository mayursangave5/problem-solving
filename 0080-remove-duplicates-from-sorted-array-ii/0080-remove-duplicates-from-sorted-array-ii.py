class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n=len(nums)
        start=1
        if n==2:
            return n
        for i in range(2,n):
            if nums[start-1]!=nums[i]:
                start+=1
                nums[start]=nums[i]

        return start+1

# 1 1 2 2 2 3 4 4 
#   s i 
# 1 1 2 2 2 3 4 4 
#     s i 
# 1 1 2 2 2 3 4 4 
#       s i
# 1 1 2 2 2 3 4 4 
#       s   i
# 1 1 2 2 3 4 4 4 
#           s i