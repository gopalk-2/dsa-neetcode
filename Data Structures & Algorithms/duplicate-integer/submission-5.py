class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq=Counter(nums)
        for num in nums:
            if freq.get(num)>1:
                return True
        return False

