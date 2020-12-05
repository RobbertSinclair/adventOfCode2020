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
            the_min = the_range[0] - 1
            the_max = the_range[1] - 1
            if (the_password[the_min] != the_password[the_max]) and (the_password[the_min] == line[1] or the_password[the_max] == line[1]):
                the_total += 1
    return the_total
            

print(solution("input.txt"))
