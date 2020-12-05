
def get_input(filename):
    line_list = []
    with open(filename) as f:
        for line in f:
            line = line.strip()
            line_list.append(line)
    return line_list

def calc_seat_id(boarding_pass):
    front_back = boarding_pass[:7]
    left_right = boarding_pass[7:]
    rows = [i for i in range(128)]
    i = 0
    for letter in front_back:
        mid = len(rows)  // 2
        if letter == "B":
            rows = rows[mid:]
        else:
            rows = rows[:mid]
    row = rows[0]
    seats = [i for i in range(8)]
    for letter in left_right:
        mid = len(seats) // 2
        if letter == "R":
            seats = seats[mid:]
        else:
            seats = seats[:mid]
    seat = seats[0]
    return row * 8 + seat

def solution(filename):
    max_id = 0
    passes = get_input(filename)
    for boarding_pass in passes:
        seat_id = calc_seat_id(boarding_pass)
        if seat_id > max_id:
            max_id = seat_id
    return max_id
        
        
        

print(solution("input.txt"))
        
            
