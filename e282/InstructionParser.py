from Instruction import Instruction
import MathUtil

'''
expect instruction in list form '[base, value]'
valid bases: 'F', '10'
return - Instruction object if valid, None if invalid
'''
def buildInstruction(instr):
    if len(instr) != 2:
        return None
    base = instr[0]
    value = instr[1]

    if base.upper() == "F":
        for char in value:
            if char != '1' and char != '0':
                return None

        return Instruction(base.upper(), value)
    elif base == '10':
        intVal = MathUtil.parseInt(value)
        if intVal is not None and intVal >= 0:
            return Instruction(base, value)

    return None

def getInstructions(inputFile):
    f = open(inputFile, 'r')
    instructionList = [];
    for line in f:
        instr = buildInstruction(line.split())
        instructionList.append(instr);
    return instructionList
