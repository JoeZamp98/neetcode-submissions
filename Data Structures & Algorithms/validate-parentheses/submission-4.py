class Solution:
    def isValid(self, s: str) -> bool:

        if (len(s) % 2) != 0:
            return False

        bracket_mapping = {
            "}": "{",
            "]": "[",
            ")": "("
        }

        stack = []

        for idx, char in enumerate(s):

            if char in bracket_mapping.values():

                stack.insert(0, char)

            elif char in bracket_mapping.keys():

                if len(stack) < 1:
                    return False

                if stack[0] == bracket_mapping[char]:

                    stack.pop(0)

                else:
                    
                    return False


            print(stack)

        if len(stack) == 0:
            return True

        else:
            return False
