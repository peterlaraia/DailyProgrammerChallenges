class Instruction:
    def __init__(self, base, value):
        self.base = base
        self.val = value

    def getBase(self):
        return self.base

    def getVal(self):
        return self.val

    def __str__(self):
        return "base: {}, value: {}".format(self.base, self.val)
