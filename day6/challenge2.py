def get_input(filename):
    the_groups = []
    with open(filename) as f:
        the_group = []
        the_group_strings = []
        for line in f:
            line = line.strip()
            if line == "":
                the_groups.append(the_group)
                the_string = "".join(the_group)
                the_group_strings.append(the_string)
                the_group = []
            else:
                the_group.append(line)
        #Add the last group
        the_string = "".join(the_group)
        the_group_strings.append(the_string)
        the_groups.append(the_group)
    return (the_groups, the_group_strings)

def solution(filename):
    the_input = get_input(filename)
    the_groups = the_input[0]
    the_strings = the_input[1]
    total_count = 0
    for i in range(len(the_groups)):
        group_set = list(set(the_strings[i]))
        for group in the_groups[i]:
            letters_to_remove = []
            for letter in group_set:
                if letter not in group:
                    letters_to_remove.append(letter)
            for letter in letters_to_remove:
                index = group_set.index(letter)
                group_set.pop(index)
        total_count += len(group_set)    
    return total_count

print(solution("input.txt"))
