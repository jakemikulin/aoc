maxRed = 12
maxGreen = 13
maxBlue = 14

def star1(lines):
    gameNo_total = 0
    for line in lines:
        impossible = 0
        (game, colon, allSets) = line.partition(":")
        gameNo = int(game.split()[1])
        sets = allSets.split(";")
        for set in sets:
            separateColours = set.split(",")
            for colour in separateColours:
                if "red" in colour:
                    redNo = int(colour.split()[0])
                    if redNo > maxRed:
                        impossible = impossible + 1
                if "green" in colour:
                    greenNo = int(colour.split()[0])
                    if greenNo > maxGreen:
                        impossible = impossible + 1
                if "blue" in colour:
                    blueNo = int(colour.split()[0])
                    if blueNo > maxBlue:
                        impossible = impossible + 1

        if impossible == 0:
            gameNo_total = gameNo_total + gameNo

    return gameNo_total

def star2(lines):
    gameTotals = []
    for line in lines:
        currentMaxRed = 0
        currentMaxGreen = 0
        currentMaxBlue = 0
        (game, colon, allSets) = line.partition(":")
        sets = allSets.split(";")
        for set in sets:
            separateColours = set.split(",")
            for colour in separateColours:
                if "red" in colour:
                    redNo = int(colour.split()[0])
                    if redNo > currentMaxRed:
                        currentMaxRed = redNo
                if "green" in colour:
                    greenNo = int(colour.split()[0])
                    if greenNo > currentMaxGreen:
                        currentMaxGreen = greenNo
                if "blue" in colour:
                    blueNo = int(colour.split()[0])
                    if blueNo > currentMaxBlue:
                        currentMaxBlue = blueNo

        gameTotals.append(currentMaxRed * currentMaxGreen * currentMaxBlue)

    return sum(gameTotals)

if __name__ == "__main__":
    with open('inputs/day02.txt') as f:
        lines = f.readlines()
    print(star1(lines))
    print(star2(lines))