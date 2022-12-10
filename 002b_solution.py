#        rck, ppr, srs
moves = ["a", "b", "c"]

def get_winner(line, total):
    input = line.split(" ")
    move_one = input[0].strip()
    index_one = moves.index(move_one)
    outcome = input[1].strip()
    
    match outcome:
        case "x":
            move_two = moves[index_one - 1]
            bonus = 0
        case "y":
            move_two = moves[index_one]
            bonus = 3
        case "z":
            if moves[index_one] == moves[-1]:
                index_one = -1
            move_two = moves[index_one + 1]
            bonus = 6 
    
    val_two = moves.index(move_two) + 1
    total += val_two + bonus

    return total

if __name__ == "__main__":
    total = 0
    with open('002_input.txt', 'r') as f:
        for line in f:
            total = get_winner(line.lower(), total)
        print(total)