class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        all_combinations = []

        nums = sorted(nums)

        for i in range(1, len(nums) - 1, 1):

            left_pointer = 0
            right_pointer = len(nums) - 1

            print(f"{left_pointer} | {i} | {right_pointer}")

            while right_pointer > left_pointer: 

                if (nums[i] + nums[right_pointer] + nums[left_pointer]) == 0:

                    sorted_triplet = sorted([nums[i], nums[right_pointer], nums[left_pointer]])

                    if sorted_triplet not in all_combinations:
                        all_combinations.append(sorted_triplet)

                    left_pointer += 1
                    right_pointer -= 1

                elif (nums[i] + nums[right_pointer] + nums[left_pointer]) > 0:

                    right_pointer -= 1

                elif (nums[i] + nums[right_pointer] + nums[left_pointer]) < 0:

                    left_pointer += 1

        return all_combinations