class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # Set left and right bounds
        l_bound = 0
        r_bound = len(nums) - 1

        # Continue in while loop so long as the bounds do not invert
        while r_bound >= l_bound:

            midpoint = l_bound + ((r_bound - l_bound) // 2)
            print(f"{l_bound} | {midpoint} | {r_bound}")

            # Special case for handling single item lists
            if len(nums) == 1:
                return 0 if nums[0] == target else -1
                
            if nums[midpoint] == target:
                return midpoint

            # Shift right bound in cases where the target is less than the midpoint value
            if target < nums[midpoint]:
                r_bound = midpoint - 1

            # Shift left bound in cases where the target is greater than the midpoint value
            if target > nums[midpoint]:
                l_bound = midpoint + 1

        return -1
            