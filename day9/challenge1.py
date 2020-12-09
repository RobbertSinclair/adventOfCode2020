def get_input(filename):
    the_list = []
    with open(filename) as f:
        for line in f:
            line = int(line.strip())
            the_list.append(line)
    return the_list

def solution(filename, pre):
    the_input = get_input(filename)
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
        
    
    
print(solution("input.txt", 25))
            
