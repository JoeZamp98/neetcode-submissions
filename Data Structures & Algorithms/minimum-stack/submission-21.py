class MinStack:

    def __init__(self):

        self.stack = []

        self.min_values = [None]
        self.max_values = [None]
        

    def push(self, val: int) -> None:   

        # Push to stack

        self.stack.append(val)

        # Update minimum value log

        current_min = self.min_values[0]

        if current_min is not None:
            if current_min < val:
                self.min_values.insert(0, current_min)
            else:
                self.min_values.insert(0, val)
        else:
            current_min = val
            self.min_values.insert(0, val)

        # print(self.stack, " | ", self.min_values)

        # Update maximum value log

        current_max = self.max_values[0]

        if current_max is not None:
            if current_max > val:
                self.max_values.insert(0, current_max)
            else: 
                self.max_values.insert(0, val)
        else:
            
            self.max_values.insert(0, val)

        # print(self.stack, " | ", self.max_values)

        # print("______________")

    def pop(self) -> None:
        
        self.stack.pop()

        del self.min_values[0]
        del self.max_values[0]

        # print(self.stack, " | ", self.min_values)

    def top(self) -> int:

        # print("MAX: ", self.max_values[0])
        
        return self.stack[-1]


    def getMin(self) -> int:
        
        # print("MIN: ", self.min_values[0])

        return self.min_values[0]
