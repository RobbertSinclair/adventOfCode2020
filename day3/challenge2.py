def find_trees(the_map, right=3, down=1):
    current_x = 0
    current_y = 0
    trees = 0
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

def get_input(filename):
    the_map = []
    with open(filename) as f:
        for line in f:
            line = line.strip()
            the_map.append(line)
    return the_map

def solution(filename):
    the_map = get_input(filename)
    right = 1
    down = 1
    num_trees = 0
    while right <= 7:
        trees = find_trees(the_map, right, down)
        print(f"Trees is {trees}")
        if num_trees == 0:
            num_trees = trees
        else:
            num_trees = num_trees * trees
        right += 2
    trees = find_trees(the_map, 1, 2)
    num_trees = num_trees * trees
    return num_trees

print(solution("input.txt"))
        
    



    
