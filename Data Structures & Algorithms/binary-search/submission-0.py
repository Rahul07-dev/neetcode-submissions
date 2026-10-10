class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1
        size=len(nums)
        left,right=0,size-1
        while left <= right:
            mid = left + (right - left) // 2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                right=mid-1
            elif target > nums[mid]:
                left=mid+1
        return -1