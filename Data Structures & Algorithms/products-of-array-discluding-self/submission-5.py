class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        left_base = [1 for x in nums]
        right_base = [1 for x in nums]
        final_base = [1 for x in nums]

        for position, x in enumerate(left_base): 
            val = left_base[position] * nums[position]
            
            if position > 0:
                val = left_base[position - 1] * nums[position]

            left_base[position] = val

        for position in range(len(right_base) - 1, -1, -1):

            val = right_base[position] * nums[position]

            if position < (len(right_base) - 1):
                val = right_base[position + 1] * nums[position]

            right_base[position] = val

        for x in range(len(final_base)): 
            
            if x == 0:
                final_base[x] = right_base[x + 1]
            
            elif x == (len(final_base) - 1): 
                final_base[x] = left_base[x - 1]

            else:
                final_base[x] = left_base[x - 1] * right_base[x + 1]

        return final_base



    

    


            
            


        
