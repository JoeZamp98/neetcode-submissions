class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l_bound = 0
        r_bound = len(nums)

        while r_bound > l_bound:

            midpoint = (r_bound - l_bound) // 2
            # print(f"{r_bound} | {l_bound} | {midpoint}")

            if nums[midpoint] == target:

                return midpoint

            if target < nums[midpoint]:

                r_bound = midpoint - 1

            if target > nums[midpoint]:

                l_bound = midpoint + 1

        return -1
            