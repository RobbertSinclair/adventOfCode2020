def get_input(filename):
    the_list = []
    with open(filename) as f:
        for line in f:
            line = int(line.strip())
            the_list.append(line)
    return the_list

def invalid_num(the_input, pre):
    i = pre
    rule_works = False
    while i < len(the_input):
        segment = the_input[i-pre:i]
        flag = False
        for item in segment:
            diff = the_input[i] - item
            if diff in segment:
                flag = True
                break
        if not flag:
            return the_input[i]
        i += 1
    return None

def solution(filename, pre):
    the_input = get_input(filename)
    invalid = invalid_num(the_input, pre)
    invalid_index = the_input.index(invalid)
    the_input = the_input[:invalid_index]
    for i in range(2, len(the_input)):
        for j in range(len(the_input)):
            segment = the_input[j:j+i]
            if len(segment) > 1 and sum(segment) == invalid:
                return min(segment) + max(segment)
    return None
             
            
        
    
    
print(solution("input.txt", 25))
            
