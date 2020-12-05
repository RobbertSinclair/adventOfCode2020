
def find_multiplication(filename):
    total_pair = []
    num_list = []
    with open(filename) as f:
        num_list = [int(line.strip()) for line in f]
    for number in num_list:
        other_num = 2020 - number
        if other_num in num_list:
            print(f"The entries were {number} and {other_num}")
            return number * other_num
    return None
        

print(find_multiplication("input.txt"))
        
