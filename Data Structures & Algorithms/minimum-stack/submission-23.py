class MinStack:

    def __init__(self):
        """
        Set this up so the stack appends to the final position, but min_values appends to the first position.  This was more intuitive in my mind, but I believe they could also run in identical directions if need be.  
        """

        self.stack = []

        self.min_values = [None]
        
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

    def pop(self) -> None:
        
        self.stack.pop()

        del self.min_values[0]

    def top(self) -> int:
        
        return self.stack[-1]


    def getMin(self) -> int:
        
        return self.min_values[0]
