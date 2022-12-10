# Lowercase item types a through z have priorities 1 through 26.
# Uppercase item types A through Z have priorities 27 through 52.

def parse_input(i, file, line_count):
    f = open(file, "r")
    lines = f.readlines()

    if i < line_count - 2:
        values = [lines[i].strip(), lines[i+1].strip(), lines[i+2].strip()]
  
        return values
 
def find_badge(values):
    for char1 in values[0]:
        for char2 in values[1]:
            if char1 == char2:
                for char3 in values[2]:
                    if char3 == char1:
                        return char3
                        
def get_sum(badge, total):
    if 97 <= ord(badge) <= 122: 
        match_value = ord(badge) - 96
        total += match_value
    if 65 <= ord(badge) <= 90:
        match_value = ord(badge) - 38          
        total += match_value
    
    return total
        
if __name__ == "__main__":
    total = 0
    i = 0
    file = "003_input.txt"
    
    with open(file, 'r') as f:
        line_count = len(f.readlines())
    while i < line_count - 2:
        bundle = parse_input(i, file, line_count)
        badge = find_badge(bundle)
        total = get_sum(badge, total)
        if i == line_count:
            break
        else:
            i += 3
            
    print(total)