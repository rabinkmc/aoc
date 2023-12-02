MAX_LIMIT = {
    "red": 12,
    "green": 13,
    "blue": 14,
}


def parse_game(line):
    line = line.strip("\n")
    game_info, game = line.split(":")
    _, id = game_info.split(" ")
    sets = game.split(";")
    max_counter = {"red": 1, "green": 1, "blue": 1}
    for _set in sets:
        for round in _set.split(","):
            num, color = round.strip(" ").split(" ")
            num = int(num)
            # if num > MAX_LIMIT[color]: // question 1
            #     return 0
            if num > max_counter[color]:
                max_counter[color] = num
    # return id question 1
    return max_counter["red"] * max_counter["green"] * max_counter["blue"]


lines = open("day2.txt").readlines()
print(sum(parse_game(line) for line in lines))
