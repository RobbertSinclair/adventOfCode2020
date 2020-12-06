def get_input(filename):
    the_groups = []
    with open(filename) as f:
        the_group = []
        for line in f:
            line = line.strip()
            if line == "":
                the_group = "".join(the_group)
                the_groups.append(the_group)
                the_group = []
            else:
                the_group.append(line)
        #Add the last group
        the_group = "".join(the_group)
        the_groups.append(the_group)
    return the_groups

def solution(filename):
    the_groups = get_input(filename)
    total_count = 0
    for group in the_groups:
        group_set = set(group)
        total_count += len(group_set)
    return total_count

print(solution("input.txt"))
                
