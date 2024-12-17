import sys



registerA = 0
registerB = 0
registerC = 0

def combo_operand(operand):
    global registerA, registerB, registerC

    if operand <= 3:
        return operand
    elif operand == 4:
        return registerA
    elif operand == 5:
        return registerB
    elif operand == 6:
        return registerC

def execute_program(program):
    global registerA, registerB, registerC

    outputStr = ''
    instruction_pointer = 0
    # print(program)
    while instruction_pointer < len(program)-1:
        # print(f'Instruction Pointer: {instruction_pointer}')
        # print(f'Register A: {registerA}')
        # print(f'Register B: {registerB}')
        # print(f'Register C: {registerC}')
        instr = program[instruction_pointer]
        operand = program[instruction_pointer+1]
        # print(f'Instruction: {instr}')
        # print(f'Operand: {operand}')
        # print(f'combo_operand: {combo_operand(operand)}')
        # input()


        if instr == 0: #adv
            num = registerA
            den = combo_operand(operand)
            registerA = num // (2 ** den)
        elif instr == 1: #bxl
            registerB = (registerB ^ operand) % 8
        elif instr == 2: #bst
            registerB = combo_operand(operand) % 8
        elif instr == 3: #jnz
            if registerA != 0:
                instruction_pointer = operand
                continue
        elif instr == 4: #bxc
            registerB = registerB ^ registerC
        elif instr == 5: #out
            outputStr += str(combo_operand(operand) % 8) + ','
            # print(outputStr)
        elif instr == 6: #bdv
            num = registerA
            den = combo_operand(operand)
            registerB = num // (2 ** den)
        elif instr == 7: #cdv
            num = registerA
            den = combo_operand(operand)
            registerC = num // (2 ** den)
        instruction_pointer += 2
    
    return outputStr[:-1]


if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        for line in f:
            if line.startswith('Register A: '):
                registerA = int(line.split(': ')[1])
            elif line.startswith('Register B: '):
                registerB = int(line.split(': ')[1])
            elif line.startswith('Register C: '):
                registerC = int(line.split(': ')[1])
            elif line.startswith('Program: '):
                program = list(map(int, line.split(': ')[1].strip().split(',')))
    
    # P1
    print(execute_program(program))


    # P2
    # The octal digits of Register A map to output digits in reverse order, with lower digits not
    # impacting them, so we can find them iteratively
    toTest = [[5], [0]]
    all_candidates = []
    while toTest:
        leadingDigits = toTest.pop(0)
        if len(leadingDigits) == len(program):
            all_candidates.append(leadingDigits)
            continue
        candidates = []
        for i in range(7, -1, -1):
            n = int('0o' + ''.join([str(x) for x in leadingDigits]) + str(i)*(len(program)-len(leadingDigits)), 8)
            registerA = n
            registerB = 0
            registerC = 0
            outputStr = execute_program(program)
            outputProgram = list(map(int, outputStr.split(',')))
            m = True
            for j in range(len(leadingDigits) + 1):
                x = len(outputProgram) - 1 - j
                if program[x] != outputProgram[x]:
                    m = False
                    break
            if m:
                toTest = [leadingDigits + [i]] + toTest

    for c in all_candidates:
        print(c)
        print(int('0o' + ''.join([str(x) for x in c]), 8))
        print()