def solution(filename, right=3, down=1):
    current_x = 0
    current_y = 0
    trees = 0
    the_map = []
    #Get the input
    with open(filename) as f:
        for line in f:
            line = line.strip()
            the_map.append(line)

    #Traverse the map
    while current_y < len(the_map):
        #Check the current position for a tree
        if the_map[current_y][current_x] == "#":
            trees += 1
        current_x += right
        #Check whether the tobaggen is out of bounds
        if current_x > len(the_map[current_y])-1:
            current_x = current_x - len(the_map[current_y])
        current_y += down
    return trees

            
            

    

print(solution("example.txt"))
