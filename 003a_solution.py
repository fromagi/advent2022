# Lowercase item types a through z have priorities 1 through 26.
# Uppercase item types A through Z have priorities 27 through 52.

def sum_dupes(line, total):
    line = line.strip()
    size = len(line)
    half_point = round(size/2)
    half_one = set(line[0:half_point])
    half_two = set(line[half_point:])

    for char1 in half_one:
        for char2 in half_two:
            if char1 == char2:
                if 97 <= ord(char1) <= 122: 
                    match_value = ord(char1) - 96
                    total += match_value
                if 65 <= ord(char1) <= 90:
                    match_value = ord(char1) - 38          
                    total += match_value
 
    return total
        
if __name__ == "__main__":
    total = 0
    with open('003_input.txt', 'r') as f:
        for line in f:
            total = sum_dupes(line, total)
        print(total)