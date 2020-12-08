def get_input(filename):
    bags = {}
    with open(filename) as f:
        for line in f:
            line = line.strip()
            line = line.replace("bags", "bag")
            line = line.split(" contain ")
            the_bags = line[1].replace(".", "").split(",")
            if len(the_bags) == 2:
                the_bags[1] = the_bags[1][1:]
            if the_bags[0] == "no other bag":
                bags[line[0]] = None
            else:
                bags[line[0]] = []
                for bag in the_bags:
                    bag = bag.strip()
                    number = int(bag[0])
                    bag_string = bag[2:]
                    bags[line[0]].append((bag_string, number))
    return bags


def lookin_bag(bag_dict, the_bag, total=0):
    if bag_dict[the_bag] == None:
        return 0
    bag_list = [bag[0] for bag in bag_dict[the_bag]]
    for bag in bag_list:
        if bag == "shiny gold bag":
            return 1
        else:
            try:
                total += lookin_bag(bag_dict, bag, total)
            except:
                return 0
    if total > 1:
        total = 1
    return total
            
def solution(filename):
    the_dict = get_input(filename)
    total = 0
    for bag in the_dict:
        if bag != "shiny gold bag":
            total += lookin_bag(the_dict, bag)
    return total
            
            
            

print(solution("input.txt"))
