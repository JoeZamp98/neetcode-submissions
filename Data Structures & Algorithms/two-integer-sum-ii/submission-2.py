class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        right_pointer = len(numbers) - 1

        if len(numbers) == 2:

            return [1, 2]

        while right_pointer >= 0:

            left_pointer = 0

            lrg_addend_candidate = numbers[right_pointer]

            if lrg_addend_candidate <= target:
                delta = target - lrg_addend_candidate

                while left_pointer <= right_pointer:
                    
                    sm_addend_candidate = numbers[left_pointer]

                    if sm_addend_candidate == delta:
                        
                        return [left_pointer + 1, right_pointer + 1]

                    left_pointer += 1

                print(f"{lrg_addend_candidate} | {sm_addend_candidate} | {delta}")

            right_pointer -= 1



