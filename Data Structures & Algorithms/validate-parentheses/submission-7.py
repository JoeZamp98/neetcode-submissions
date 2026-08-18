class Solution:
    def isValid(self, s: str) -> bool:
        
        # If the length of the string is odd, it is automatically invalid since we know all parentheticals must be in a pair of two.  
        if (len(s) % 2) != 0:
            return False

        bracket_mapping = {
            "}": "{",
            "]": "[",
            ")": "("
        }

        stack = []

        #Iterate over the string
        for idx, char in enumerate(s):

            #If the character is in the opening group, insert it at the beginning of the stack
            if char in bracket_mapping.values():

                stack.insert(0, char)

            # If the character is in the closing group, test whether its complimentary opening character is at the top of the stack.  If so, pop it from the stack.  Since we're only adding opening parentheses to the stack, the valid character should always be at the top of the stack, even if there have been other closing characters between it and its corresponding opening version.  
            elif char in bracket_mapping.keys():

                if len(stack) < 1:
                    return False

                if stack[0] == bracket_mapping[char]:

                    stack.pop(0)

                else:
                    
                    return False

            print(stack)

        # If the length of the stack after the full string iteration is 0, it should be valid
        if len(stack) == 0:
            return True

        else:
            return False
