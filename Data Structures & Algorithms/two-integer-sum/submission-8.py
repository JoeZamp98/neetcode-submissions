class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        all_seen_nums = {} #idx, num

        for idx, x in enumerate(nums):

            all_seen_nums[idx] = x

            difference = target - x

            possible_pair = {k: v for k, v in all_seen_nums.items() if v == difference}

            if possible_pair:

                diff_idx = [k for k, v in possible_pair.items()][0]
                diff_value = [v for k, v in possible_pair.items()][0]

                if diff_idx != idx:

                    return [diff_idx, idx]

        return []


        