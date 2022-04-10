class Solution:
    def minMoves(self, nums: List[int]) -> int:
        number_of_moves = sum(nums) - len(nums) * min(nums)
        return number_of_moves
        