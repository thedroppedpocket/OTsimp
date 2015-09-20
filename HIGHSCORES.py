def highScoresE(Player):
    infile = open("highScoresE.txt", "r")
    highScores = list()
    for line in infile:
        highScores.append(line)
        infile.close()
        highScores.sort()
        name = Player.getNames()[0]
        score = (str(Player.getDay()) + " : " + name + "\n")
    highScores.append(score)
    highScores.sort()
    if len(highScores) > 10:
        highScores.remove(highScores[-1])
        print("HIGH SCORES")
    for b in range(len(highScores)):
        print(highScores[b])

    outfile = open("highScoresE.txt", "w")
    for a in range(len(highScores)):
        outfile.write(highScores[a])
    outfile.close()


def highScoresH(Player):
    infile = open("highScoresH.txt", "r")
    highScores = list()
    for line in infile:
        highScores.append(line)
        infile.close()
        highScores.sort()
        name = Player.getNames()[0]
        score = (str(Player.getDay()) + " : " + name + "\n")
    highScores.append(score)
    highScores.sort()
    if len(highScores) > 10:
        highScores.remove(highScores[-1])
        print("HIGH SCORES")
    for b in range(len(highScores)):
        print(highScores[b])

    outfile = open("highScoresH.txt", "w")
    for a in range(len(highScores)):
        outfile.write(highScores[a])
    outfile.close()

