def find_multiplication(filename):
    total_pair = []
    num_list = []
    with open(filename) as f:
        num_list = [int(line.strip()) for line in f]
    for number in num_list:
        new_total = 2020 - number
        for other_num in num_list:
            third_num = new_total - other_num
            if third_num in num_list:
                print(f"The solution is {number}, {other_num} and {third_num}")
                return number * other_num * third_num
    return None
        

print(find_multiplication("input.txt"))
