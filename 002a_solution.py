p1 = ["a", "b", "c"]
p2 = ["x", "y", "z"]

def get_winner(line, total):
    moves = line.split(" ")
    move_one = moves[0].strip()
    move_two = moves[1].strip()
    val_one = p1.index(move_one) + 1
    val_two = p2.index(move_two) + 1

    if (val_two == val_one):
        total += val_two + 3      
    elif (move_two == "x" and move_one == "c") or (move_two == "y" and move_one == "a") or (move_two == "z" and move_one == "b"):
        total += val_two + 6
    else:
        total += val_two

    return total

if __name__ == "__main__":
    total = 0
    with open('002_input.txt', 'r') as f:
        for line in f:
            total = get_winner(line.lower(), total)
        print(total)