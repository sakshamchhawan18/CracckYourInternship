class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            sum_target = nums[i] + nums[i+1]
            if sum_target == target:
                return (i,i+1)
        