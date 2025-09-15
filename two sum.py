def twoSum(self, nums: List[int], target: int) -> List[int]:
    has={}
    for i in range(len(nums)):
        comp=target-nums[i]
        if comp in has:
            return [has[comp],i]
        has[nums[i]]=i