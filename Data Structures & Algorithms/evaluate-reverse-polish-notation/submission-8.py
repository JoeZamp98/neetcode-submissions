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

            if tokens[x] not in list(operator_mapping.keys()):

                # print(tokens[x])

                running_stack.append(tokens[x])

            else:

                # print(tokens[x])

                second_digit = int(running_stack.pop(-1))
                first_digit = int(running_stack.pop(-1))

                result = operator_mapping[tokens[x]](first_digit, second_digit)

                running_stack.append(result)

            # print(running_stack)

        return int(running_stack[0])