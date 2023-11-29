
choice_map = {"A": "rock", "B": "paper", "C": "scissor"}
points_map = {"A": 1, "B": 2, "C": 3}

def get_score(player_action, opponent_choice):
    if player_action == "Y":
        return 3 + points_map[opponent_choice]
    elif player_action == "X":
        choice = ""
        if opponent_choice == "A":
            choice = "C"
        elif opponent_choice == "B":
            choice = "A"
        else:
            choice = "B"
        return 0 + points_map[choice]
    else:
        choice = ""
        if opponent_choice == "A":
            choice = "B"
        elif opponent_choice == "B":
            choice = "C"
        else:
            choice = "A"
        return 6 + points_map[choice]

def solve():
    score = 0
    with open("input.txt", "r") as f:
        for line in f.readlines():
            if line == "\n":
                return score
            line = line.strip()
            score += get_score(line[-1], line[0])

print(solve())
