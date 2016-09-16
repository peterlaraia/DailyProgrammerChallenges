class FibonacciGenerator:
    sequence = []
    maxSum = 0


    def __init__(self):
        self.sequence = [1, 1]
        maxSum = 2

    def until(self, until):
        take = self.sequence[-2]
        plus = self.sequence[-1]
        
        fib = self.sequence[-1]
        while fib < until:
            fib = take + plus
            self.sequence.append(fib)
            self.maxSum += fib
            take = plus
            plus = fib

    def untilMaxSum(self, until):
        take = self.sequence[-2]
        plus = self.sequence[-1]

        fib = self.sequence[-1]
        while self.maxSum < until:
            fib = take + plus
            self.sequence.append(fib)
            self.maxSum += fib
            take = plus
            plus = fib

    def count(self, steps):
        take = self.sequence[-2]
        plus = self.sequence[-1]
        
        for i in range(0, steps):
            fib = take + plus
            self.sequence.append(fib)
            self.maxSum += fib
            take = plus
            plus = fib

    def __str__(self):
        return "sequence: {}, maxSum: {}".format(self.sequence, self.maxSum)
