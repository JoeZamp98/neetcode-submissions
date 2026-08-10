class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return 1

        position = 0

        nums = sorted(list(set(nums)))

        runs = []
        run = 1

        while position < len(nums) - 1:
            
            curr_num = nums[position]
            next_num = nums[position + 1]

            if next_num == curr_num + 1:

                position += 1
                run += 1

                # print("Curr: ", curr_num, " Next: ", next_num)
                runs.append(run)

            else: 

                runs.append(run)

                position += 1
                run = 1
        
        return max(runs) if runs else 1
        
