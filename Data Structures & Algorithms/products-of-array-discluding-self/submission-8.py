class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        left_base = [1 for x in nums]
        right_base = [1 for x in nums]
        final_base = [1 for x in nums]

        standard_len = len(final_base) - 1

        for position, x in enumerate(left_base): 
            
            if position > 0:
                val = left_base[position - 1] * nums[position]
            else:
                val = left_base[position] * nums[position]

            left_base[position] = val

        for position in range(standard_len, -1, -1):

            if position < (standard_len):
                val = right_base[position + 1] * nums[position]
            else:
                val = right_base[position] * nums[position]

            right_base[position] = val

        for x in range(standard_len + 1): 
            
            if x == 0:
                final_base[x] = right_base[x + 1]
            
            elif x == (standard_len): 
                final_base[x] = left_base[x - 1]

            else:
                final_base[x] = left_base[x - 1] * right_base[x + 1]

        return final_base



    

    


            
            


        
