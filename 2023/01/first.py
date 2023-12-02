def findCalibrationValue(line: str) -> int:
    for firstIndex in range(len(line)):
        if line[firstIndex].isdigit():
            break

    for lastIndex in range(len(line) - 1, firstIndex - 1, -1):
        if line[lastIndex].isdigit():
            break

    calibrationValueString: str = line[firstIndex] + line[lastIndex]

    return int(calibrationValueString)


with open("./input", "r") as input:
    sum: int = 0

    for line in input:
        calibrationValue = findCalibrationValue(line)
        print(line[:-1] + " : " + str(calibrationValue))
        sum += calibrationValue

    print(sum)
