def get_input(filename):
    instructions = []
    with open(filename) as f:
        for line in f:
            line = line.strip()
            line = line.split(" ")
            if line[1][0] == "+":
                line[1] = int(line[1][1:])
            else:
                line[1] = int(line[1])
            line.append(False)
            instructions.append(line)
    return instructions


def run_instructions(instructions):
    i = 0
    accutator = 0
    increment = 1
    while i < len(instructions) and not instructions[i][2]:
        the_instruction = instructions[i][0]
        if the_instruction == "nop":
            increment = 1
        elif the_instruction == "jmp":
            increment = instructions[i][1]
        else:
            accutator += instructions[i][1]
            increment = 1
        instructions[i][2] = True
        i += increment
    if i >= len(instructions):
        return (accutator, True)
    else:
        return (accutator, False)

def solution(filename):
    instructions = get_input(filename)
    nop_index = [i for i in range(len(instructions)) if instructions[i][0] == "nop"]
    jmp_index = [i for i in range(len(instructions)) if instructions[i][0] == "jmp"]
    accutator = 0
    finished = False
    for index in nop_index:
        temp_instructions = [instruction.copy() for instruction in instructions]
        temp_instructions[index][0] = "jmp"
        accutator, finished = run_instructions(temp_instructions)
        if finished:
            return accutator
    for index in jmp_index:
        temp_instructions = [instruction.copy() for instruction in instructions]
        temp_instructions[index][0] = "nop"
        accutator, finished = run_instructions(temp_instructions)
        if finished:
            return accutator
    return None
            
print(solution("input.txt"))
            
