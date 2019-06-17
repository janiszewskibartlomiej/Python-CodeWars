def points(game):
    score = 0
    for element in game:
        x = int(element[0])
        y = int(element[2])
        if x > y:
            score+= 3
        if x == y:
            score += 1
    return score
