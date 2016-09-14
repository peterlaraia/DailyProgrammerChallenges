#!/usr/bin/python3
import sys
import Messages as messages
import InstructionParser as parser
from FibonacciGenerator import FibonacciGenerator

def fromFibonacciToBaseTen(fibStorage, sequence):
    if len(sequence) > len(fibStorage):
        fibStorage = fibStorage + FibonacciGenerator(fibStorage[-2], fibStorage[-1]).count(len(sequence) - len(fibStorage))
    baseTenVal = 0
    for i, c in enumerate(reversed(sequence)):
        if c == "1":
            baseTenVal += fibStorage[i]
    return baseTenVal, fibStorage

def main():
    if len(sys.argv) != 2:
        print(messages.usage(sys.argv))
        exit(-1)

    fibStorage = [1, 1]

    generator = FibonacciGenerator(1, 1)

    fibSequence = generator.until(100)

    instructions = parser.getInstructions(sys.argv[1])
    for instr in instructions:
        print(instr)
        if instr.getBase() == "F":
            out, fibStorage = fromFibonacciToBaseTen(fibStorage, instr.getVal())
            print(out)

if __name__ == "__main__":
    main()
