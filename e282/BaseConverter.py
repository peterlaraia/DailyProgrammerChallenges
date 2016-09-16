#!/usr/bin/python3
import sys
import Messages as messages
import InstructionParser as parser
from FibonacciGenerator import FibonacciGenerator

def fromFibonacciToBaseTen(fibGen, sequence):
    if len(sequence) > len(fibGen.sequence):
        fibGen.count(len(sequence) - len(fibGen.sequence))
    baseTenVal = 0
    for i, c in enumerate(reversed(sequence)):
        if c == "1":
            baseTenVal += fibGen.sequence[i]
    return baseTenVal

def fromBaseTenToFib(fibGen, baseTenVal):
    if baseTenVal > fibGen.maxSum:
        fibGen.untilMaxSum(baseTenVal)
    fibString = ''

    for i in reversed(fibGen.sequence):
        if i > baseTenVal and len(fibString) > 0:
            fibString += '0'
        else:
            fibString += '1'
            baseTenVal -= i

    return fibString

def main():
    if len(sys.argv) != 2:
        print(messages.usage(sys.argv))
        exit(-1)

    fibGenerator = FibonacciGenerator()

    instructions = parser.getInstructions(sys.argv[1])
    for instr in instructions:
        if instr.getBase() == "F":
            out = fromFibonacciToBaseTen(fibGenerator, instr.getVal())
            print(out)
        elif instr.getBase() == "10":
            out = fromBaseTenToFib(fibGenerator, instr.getVal())
            print(out)

if __name__ == "__main__":
    main()
