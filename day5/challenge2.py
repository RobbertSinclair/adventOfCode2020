
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
    passes = get_input(filename)
    seat_ids = sorted([calc_seat_id(the_pass) for the_pass in passes])
    i = 0
    while i < len(seat_ids)-1:
        first = seat_ids[i]
        last = seat_ids[i+1]
        difference = last - first
        if difference == 2:
            return last - 1
        i += 1
        
        
        
        
        

print(solution("input.txt"))
        
            
