class FibonacciGenerator:

    def __init__(self, base, add):
        self.base = base
        self.add = add 
        self.sequence = []

    def until(self, until, includeInit=False):
        take = self.base
        plus = self.add
        if take < 0 or plus < 0:
            return []
        else:
            self.sequence = [take, plus] if includeInit else []
        
        fib = take + plus
        while fib < until:
            self.sequence.append(fib)
            take = plus
            plus = fib
            fib = take + plus
        return self.sequence

    def count(self, steps, includeInit=False):
        take = self.base
        plus = self.add
        if take < 0 or plus < 0:
            return []
        else:
            self.sequence = [take, plus] if includeInit else []

        for i in range(0, steps):
            fib = take + plus
            self.sequence.append(fib)
            take = plus
            plus = fib
        return self.sequence

    def __str__(self):
        return "base: {}, add: {}, sequence: {}".format(self.base, self.add, self.sequence)
