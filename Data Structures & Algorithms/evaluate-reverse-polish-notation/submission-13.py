import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        operator_mapping = {
            "*": operator.mul,
            "-": operator.sub,
            "+": operator.add,
            "/": operator.truediv
        }

        running_stack = []

        for x in range(len(tokens)):

            # Append numbers to a running stack
            if tokens[x] not in list(operator_mapping.keys()):
                running_stack.append(tokens[x])

            # When an operator is reached, apply it to the two prior numbers and remove them from the stack, replacing with the result
            else:
                second_digit = int(running_stack.pop(-1))
                first_digit = int(running_stack.pop(-1))

                result = operator_mapping[tokens[x]](first_digit, second_digit)

                running_stack.append(result)

        return int(running_stack[0])