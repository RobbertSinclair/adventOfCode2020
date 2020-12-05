import re

def create_passport(passport_list):
    passport = {}
    for term in passport_list:
        term = term.split(":")
        passport[term[0]] = term[1]
    return passport

def parse_data(filename):
    passports = {}
    new_passport = []
    i = 0
    with open(filename) as f:
        for line in f:
            line = line.strip()
            if line == "":
                passports[i] = create_passport(new_passport)
                new_passport = []
                i += 1
            else:
                new_passport = new_passport + line.split(" ")
                
    return passports

def validate_passport(passport):
    valid_eye_colours = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    #Validate integer only fields
    #Check whether they are integers
    try:
        birth_year = int(passport["byr"])
        issue_year = int(passport["iyr"])
        exp_year = int(passport["eyr"])
    except:
        return False
    #Check that the integer values are valid
    if (birth_year < 1920 or birth_year > 2002) or (issue_year < 2010 or issue_year > 2020) or (exp_year < 2020 or exp_year > 2030):
        return False
    #Validate Height
    height = passport["hgt"]
    height_ending = height[-2:]
    try:
        length = int(height.replace(height_ending, ""))
    except:
        return False
    #Finally check whether the height is valid
    if height_ending == "cm":
        if length < 150 or  length > 193:
            return False
    elif height_ending == "in":
        if length < 59 or length > 76:
            return False
    else:
        return False
    #Validation of the hair
    hair_colour = passport["hcl"]
    if hair_colour[0] != '#':
        return False
    hair_list = [char for char in hair_colour[1:] if char.isalpha() or char.isdigit()]
    if len(hair_colour[1:]) != 6 and len(hair_list) != 6:
        return False
    #Validation of eye colour
    if passport["ecl"] not in valid_eye_colours:
        return False
    #Finally validate the passport index
    passport_id = passport["pid"]
    passport_check = [char for char in passport_id if char.isdigit()]
    if len(passport_id) != 9 or len(passport_check) != 9:
        return False
    return True
    
    
def solution(filename):
    valid_passports = 0
    the_passports = parse_data(filename)
    valid1 = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"}
    valid2 = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
    for passport in the_passports:
        passKeys = set(the_passports[passport].keys())
        if (passKeys == valid1 or passKeys == valid2) and validate_passport(the_passports[passport]):
            valid_passports += 1
    return valid_passports
            
    

print(solution("input.txt"))
