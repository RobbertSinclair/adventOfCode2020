def solution(filename):
    the_total = 0
    #Get the file
    with open(filename) as f:
        for line in f:
            line = line.strip()
            line = line.replace(":", "")
            line = line.split(" ")
            #Get the range of numbers
            the_range = [int(number) for number in line[0].split("-")]
            the_password = line[2]
            if the_password.count(line[1]) in range(the_range[0], the_range[1]+1):
                the_total += 1
    return the_total
            

print(solution("input.txt"))
        
    
