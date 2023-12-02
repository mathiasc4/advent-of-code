MAX_R_COUNT: int = 12
MAX_G_COUNT: int = 13
MAX_B_COUNT: int = 14


def isGamePossible(sets: list[tuple[int, int, int]]) -> bool:
    highestCubeCounts: tuple[int, int, int] = findHighestCubeCounts(sets)

    return (
        (highestCubeCounts[0] <= MAX_R_COUNT)
        and (highestCubeCounts[1] <= MAX_G_COUNT)
        and (highestCubeCounts[2] <= MAX_B_COUNT)
    )


def findHighestCubeCounts(sets: list[tuple[int, int, int]]) -> tuple[int, int, int]:
    highestRedCount: int = -1
    highestGreenCount: int = -1
    highestBlueCount: int = -1

    for set in sets:
        redCount: int = set[0]
        greenCount: int = set[1]
        blueCount: int = set[2]

        if redCount > highestRedCount:
            highestRedCount = redCount

        if greenCount > highestGreenCount:
            highestGreenCount = greenCount

        if blueCount > highestBlueCount:
            highestBlueCount = blueCount

    return (highestRedCount, highestGreenCount, highestBlueCount)


def parseSetString(setString: str) -> tuple[int, int, int]:
    redCount: int = 0
    greenCount: int = 0
    blueCount: int = 0

    cubesList: list[str] = setString.split(", ")

    for cubes in cubesList:
        split: list[str] = cubes.split(" ")

        count: int = int(split[0])
        color: str = split[1]

        if color == "red":
            redCount = count

        if color == "green":
            greenCount = count

        if color == "blue":
            blueCount = count

    return (redCount, greenCount, blueCount)


def parseSetsString(setsString: str) -> list[tuple[int, int, int]]:
    return list(map(parseSetString, setsString.split("; ")))


def parseGameString(gameString: str) -> tuple[int, list[tuple[int, int, int]]]:
    split: list[str] = gameString.split(": ")

    gameID: int = int(split[0].split(" ")[1])
    sets: list[tuple[int, int, int]] = parseSetsString(split[1])

    return (gameID, sets)


with open("./input", "r") as input:
    sum: int = 0

    for line in input:
        line = line.strip()
        gameID, sets = parseGameString(line)

        isPossible: bool = isGamePossible(sets)

        print(str(gameID) + " : " + str(isPossible) + " : " + str(findHighestCubeCounts(sets)))

        if isPossible:
            sum += gameID

    print(sum)
