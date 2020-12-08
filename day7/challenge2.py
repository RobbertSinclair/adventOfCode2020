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
        return 1
    total = 0
    bag_list = bag_dict[the_bag]
    for bag in bag_list:
        amount = bag[1]
        bag_name = bag[0]
        total += lookin_bag(bag_dict, bag_name, total) * amount
    return total
        
        





def solution(filename):
    bag_dict = get_input(filename)
    bag = "shiny gold bag"
    return lookin_bag(bag_dict, bag)
    


bag_dict = get_input("example2.txt")
print(bag_dict)
